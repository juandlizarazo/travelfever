import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from matplotlib import rc
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
        newdf = newdf.iloc[2:]
        newdf.columns = ['country', 'population', 'change', 'rank']
        subdf.append(newdf)

        newdf = df[col_names[14:17]]
        newdf = newdf.iloc[2:]
        newdf.columns = ['country', 'population', 'change']
        subdf.append(newdf)
        data_by_month[sheet] = subdf
    return data_by_month

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

    return read_port_entry()


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

def main():
    read_other_disease()


if __name__ == "__main__":
    main()
