import pandas as pd
import sys
import pandas_profiling
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(path):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv("C:/Users/vong2/OneDrive/Desktop/data301/project-group28-project/data/raw/Fat_Supply_Quantity_Data.csv")
          .iloc[:, [0,24,26,27,28,29,30] ]
        
        
          # etc...
          )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
            df1
            .assign(Total_Confirmed_Cases = lambda x: x.Population * x.Confirmed * 0.01)
            .assign(Total_Active_Cases = lambda x: x.Population * x.Active * 0.01) 
            .dropna()
            .reset_index(drop=True)
            )
               


    # Make sure to return the latest dataframe

    return df2 


test = df2[["Country","Obesity","Total_Active_Cases"]]

test.describe(exclude=np.object).T


profile = pandas_profiling.ProfileReport(test)
display(profile)


test = test.assign(size = lambda x: np.where((x.Total_Active_Cases > 50000), "above","below"))

#order_test = (test
                 #.groupby('size')["Obesity"]
                 #.mean()
                 #.round(2)
                 #.sort_values(ascending=False)
                 #.reset_index()
             #)