import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from matplotlib import rc
import geopandas as gpd
rc('lines', linewidth=2)
rc('font', size=18)


def read_quick_release():
    xl = pd.ExcelFile("../US_arrivals_data/COR Quick Release.xlsx")
    sh_names = xl.sheet_names

    data_by_month = dict()
    for sheet in sh_names[:-1]:
        subdf = []
        df = xl.parse(sheet)
        col_names = df.columns
        newdf = df[list(col_names[:4]) + list(col_names[5:8])]
        newdf = newdf.iloc[3:]
        newdf.columns = ['country', 'population', 'ratio', 'change',\
                'ytd_population', 'ytd_ratio', 'ytd_change']
        newdf = newdf.dropna()
        subdf.append(newdf)

        newdf = df[col_names[9:13]]
        newdf = newdf.iloc[1:]
        newdf.columns = ['country', 'population', 'change', 'rank']
        subdf.append(newdf)

        newdf = df[col_names[14:17]]
        newdf = newdf.iloc[2:]
        newdf.columns = ['country', 'population', 'change']
        subdf.append(newdf)
        data_by_month[sheet] = subdf
    return data_by_month

def parse_quick_release():
    data_by_month = read_quick_release()
    china, japan = [], []
    for key in data_by_month.keys():
        df = data_by_month[key][1]
    #    print(df)
        china.append(df[df['country'] == 'CHINA, PRC']['population'].to_numpy())
        japan.append(df[df['country'] == 'JAPAN']['population'].to_numpy())
    plt.plot(np.arange(1, 12,1), china, 'r', marker='o', label='China, PRC')
    plt.plot(np.arange(1, 12,1), japan, 'k', marker='d', label='Japan')
    plt.ylim([1e4, 5e5])
    plt.tight_layout()
    plt.legend()
    plt.xlabel('Month')
    plt.ylabel('Number of arrivals')
    plt.savefig('../figs/jn_ch_arrivals.png')
    plt.show()

def read_port_entry():
    xl = pd.ExcelFile("../US_arrivals_data/Final COR Port of Entry.xlsx")
    sh_names = xl.sheet_names

    data_by_year = dict()
    for sheet in sh_names:
        df = xl.parse(sheet)
        col = df.iloc[0]
        df = df.iloc[4:]
        df.columns = col
        df = df.dropna(axis=1, how='all')
        df = df.dropna(axis=0, how='any')
        data_by_year[sheet] = df

    return data_by_year


def read_volume():
    xl = pd.ExcelFile("../US_arrivals_data/Final COR Volume.xlsx")
    sh_names = xl.sheet_names

    data_by_year = dict()
    end = 2
    for sheet in sh_names[1:end]:
        df = xl.parse(sheet)
        df = df.dropna(axis=1, how='all')
        df = df.dropna(axis=0, how='any')
        col = df.iloc[0]
        df = df.iloc[1:]
        df.columns = col
        data_by_year[sheet] = df

    return data_by_year


def read_other_disease():
    xl = pd.ExcelFile("../US_arrivals_data/sick_people_number.xlsx")
    died = defaultdict(list)
    entry, res = dict(), []
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)
        df = df.dropna(axis=0, how='any')
        #data = df.loc[:, ['Year', 'Num of people died', 'Africa entry to US']].values
        data = df.loc[:, ['Year', 'Num of people died', 'Total entry to US']].values
        for i in range(len(data)):
            died[data[i, 0]].append(data[i, 1])
            entry[data[i, 0]] = data[i, 2]
        for keys in died.keys():
            res.append( [sum(died[keys]), entry[keys]] )
    res = np.array(res)
    x = res[:, 0].reshape((-1, 1))
    y = res[:, 1].reshape((-1, 1))
    kernel = DotProduct() + WhiteKernel()
    gpr = GaussianProcessRegressor(kernel=kernel, random_state=1).fit(x, y)
    x_pred = np.linspace(min(x), max(x), 100)
    y_pred, s_pred = gpr.predict(x_pred, return_std=True)
    x_pred = x_pred.reshape(-1)
    y_ref = np.ones(x_pred.shape)*y_pred[0]
    y_pred = y_pred.reshape(-1)
    plt.scatter(x, y, edgecolor='k', color='k', label='Training data')
    plt.plot(x_pred, y_pred, color='r', label='GP prediction')
    plt.plot(x_pred, y_ref, 'g--', label='Reference')
    plt.ylim([6.5e7, 8e7])
    plt.xlabel('Death toll in outbreak country/area')
    plt.ylabel('# International entries to US')
    plt.fill_between(x_pred, y_pred-s_pred, y_pred+s_pred, alpha=0.2,\
            edgecolor='#3F7F4C', facecolor='#7EFF99')
    plt.tight_layout()
    plt.legend()
    plt.savefig('../figs/death_entry_prediction.png')
    plt.show()


def parse_ports_entry():
    data_by_year = read_port_entry()
    keys = list(data_by_year.keys())
    df = data_by_year[keys[0]].iloc[:, 1:10]
    col = list(df.columns)
    col[0] = 'state'
    df.columns=col
    s = df.state
    df.state = df['state'].apply(lambda x: x.split(',')[-1].strip())
    entry = df.groupby('state', as_index=False).sum()
    
    usa = gpd.read_file('../data/states/states.shp')
    pd_usa = pd.DataFrame(usa)
    pd_col = list(pd_usa.columns)
    pd_usa.columns = ["state" if x == "STATE_ABBR" else x for x in pd_col]
    merged = pd.merge(how='outer', left=pd_usa, right=entry, left_on='state', right_on='state')
    merged = merged.iloc[:51]
    merged = merged.fillna(0)
    merged.columns = [str(x) for x in list(merged.columns)]
    merged = gpd.GeoDataFrame(merged)
    merged.plot(column='2011.0', legend=True)
    plt.show()


def main():
    parse_ports_entry()


if __name__ == "__main__":
    main()
