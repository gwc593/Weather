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

    # data_loc = 'Data/Lowestoft_Data.txt'
    data_loc = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/lowestoftdata.txt"
    df = pd.read_csv(data_loc, skiprows=range(0,6))
    print(df.iloc[-1:])


# ## Format dataframe
#     df['Date'] = pd.to_datetime(dict(year=df.Year, month=df.Month, day='01'))
#
#     df.reset_index()
#     df.index = df['Date']
#
#     del df['Date']
#
#     years = df['Year'].tolist()
#     years = make_unique(years)
#     months = np.linspace(1, 12, 12)









## Plotting

    ## Full plot
    # plt.style.use('dark_background')
    # plot1 = plt.figure()
    #  ax = plot1.add_subplot(2 ,1, 1)
    # for i in months:
    #     ax.plot(df['Tmax'].loc[df['Month']==i], alpha=0.5, label=i)
    # plt.legend(loc='best')
    # ax.set_title("Temperature by Each Month", fontweight="bold")
    #
    # july = df['Tmax'].loc[df['Month']==7]
    # error = np.std(july)
    # mean = np.mean(july)
    #
    # df['error_july'] = error
    # df['mean_july'] = mean
    #
    #
    #
    # # July Spread
    # ax = plot1.add_subplot(2 ,2, 4, sharex=ax)
    # ax.plot(df['Tmax'].loc[df['Month']==7], 'fuchsia', alpha=1, label="July")
    # ax.plot(df['mean_july'].loc[df['Month'] == 7]+1*df['error_july'].loc[df['Month'] == 7], 'r-', alpha=0.25, label="Threshold (%68.2)")
    # ax.plot(df['mean_july'].loc[df['Month'] == 7]-1*df['error_july'].loc[df['Month'] == 7], 'r-', alpha=0.25)
    # ax.plot(df['mean_july'].loc[df['Month'] == 7]+2*df['error_july'].loc[df['Month'] == 7], 'r-', alpha=0.55, label="Threshold (%95.4)")
    # ax.plot(df['mean_july'].loc[df['Month'] == 7]-2*df['error_july'].loc[df['Month'] == 7], 'r-', alpha=0.55)
    # ax.plot(df['mean_july'].loc[df['Month'] == 7]+3*df['error_july'].loc[df['Month'] == 7], 'r-', alpha=0.90, label="Threshold (%99.9)")
    # ax.plot(df['mean_july'].loc[df['Month'] == 7]-3*df['error_july'].loc[df['Month'] == 7], 'r-', alpha=0.90)
    # ax.plot(df['mean_july'].loc[df['Month'] == 7], 'g-', alpha=1.0, label="Mean Average")
    #
    #
    # plt.legend(loc=4)
    # ax.set_title("July Temperatures", fontweight="bold")
    #
    # # max min spectrum
    # ax = plot1.add_subplot(2, 2, 3)
    # for i in years:
    #     ax.plot(df['Month'].loc[df['Year'] == i ], df['Tmax'].loc[df['Year'] == i], 'r-', alpha=(0.008737864*i-16.62427184), label=i)
    #     ax.plot(df['Month'].loc[df['Year'] == i], df['Tmin'].loc[df['Year'] == i], 'b-', alpha=(0.008737864 * i - 16.62427184), label=i)
    # ax.set_title("Max / Min Temperature spectrum", fontweight="bold")
    # # plt.legend()
    #
    #
    # plt.show()

