import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_unique(mylist):
    temp_list = mylist
    mylist = []
    for i in temp_list:
        if i not in mylist:
            mylist.append(i)
    return mylist


if __name__ == "__main__":

    data_loc = 'Data/Lowestoft_Data.csv'

    df = pd.read_csv(data_loc)
    df['Date'] = pd.to_datetime(dict(year=df.Year, month=df.Month, day='01'))

    df.reset_index()
    df.index = df['Date']

    del df['Date']

    years = df['Year'].tolist()
    years = make_unique(years)
    months = np.linspace(1, 12, 12)

    plt.style.use('dark_background')
    plot1 = plt.figure()


    ax = plot1.add_subplot(2 ,1, 1)
    for i in months:
        ax.plot(df['Tmax'].loc[df['Month']==i], alpha=0.5, label=i)
    plt.legend(loc='best')
    ax.set_title("Temperature by Each Month", fontweight="bold")

    ax = plot1.add_subplot(2 ,2, 4)
    ax.plot(df['Tmax'].loc[df['Month']==7], 'fuchsia', alpha=0.5, label="July")
    plt.legend(loc='best')
    ax.set_title("July Temperatures", fontweight="bold")


    # plot2 = plt.figure()
    ax = plot1.add_subplot(2, 2, 3)
    for i in years:
        ax.plot(df['Month'].loc[df['Year'] == i ], df['Tmax'].loc[df['Year'] == i], 'r-', alpha=(0.008737864*i-16.62427184), label=i)
        ax.plot(df['Month'].loc[df['Year'] == i], df['Tmin'].loc[df['Year'] == i], 'b-', alpha=(0.008737864 * i - 16.62427184), label=i)
    ax.set_title("Max / Min Temperature spectrum", fontweight="bold")
    # plt.legend()


    # # plot3 = plt.figure()
    # ax = plot1.add_subplot(2, 2, 4)
    # for i in years:
    #     ax.plot(df['Month'].loc[df['Year'] == i ], df['Tmin'].loc[df['Year'] == i], 'b-', alpha=(0.008737864*i-16.62427184), label=i)
    # # plt.legend()
    # ax.set_title("Max Temperature spectrum", fontweight="bold")
    plt.show()

