import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



if __name__ == "__main__":

    data_loc = 'Data/Lowestoft_Data.csv'

    df = pd.read_csv(data_loc)
    df['Date'] = pd.to_datetime(dict(year=df.Year, month=df.Month, day='01'))

    df.reset_index()
    df.index=df['Date']

    del df['Date']
    del df['Year']
    del df['Month']


    plot1 = plt.figure()
    ax = plot1.add_subplot(1, 1, 1)
    ax.plot(df['Tmax'], 'r-', alpha=0.5)
    ax.plot(df['Tmin'], 'b-', alpha=0.5)


    plt.show()

