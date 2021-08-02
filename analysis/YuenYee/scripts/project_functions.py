import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(path_kg, path_kcal):
    
    # Method Chain 1 for path_kg (Load data, select relevant columns, rename columns, drop missing values)
    
    df1 = (pd.read_csv(path_kg)[['Country','Stimulants','Confirmed','Deaths','Recovered','Active','Population']]
           .rename(columns = {'Stimulants':'% Stimulants (kg)','Confirmed':'% Confirmed','Deaths':'% Deaths','Recovered':'% Recovered','Active':'% Active'})
           .dropna()
           .reset_index()
           .drop(['index'],axis=1)
            
    )
                        
    
    # Method Chain 2 for path_kcal (Load data, drop missing values, rename column, drop columns to leave only 'Stimulants' in df
                              
    df2 = (pd.read_csv(path_kcal)[['Country','Stimulants','Confirmed','Deaths','Recovered','Active','Population']]
           .dropna()
           .reset_index()
           .rename(columns = {'Stimulants':'% Stimulants (kcal)'})
           .drop(['index','Country','Confirmed','Deaths','Recovered','Active','Population'],axis=1)
    
    )
    
    # Method Chain 3 (combine both dataframes and reorder columns)
    
    df3 = (pd.concat([df1,df2],axis=1)
           .reindex(columns=['Country','% Stimulants (kg)','% Stimulants (kcal)','% Confirmed','% Deaths','% Recovered','% Active','Population'])
          
    )
    
    return df3

load_and_process('C:\\Users\\lyuen\\OneDrive\\desktop\\Data301\\Project\\project-group28-project\\data\\raw\\Food_Supply_Quantity_kg_Data.csv','C:\\Users\\lyuen\\OneDrive\\desktop\\Data301\\Project\\project-group28-project\\data\\raw\\Food_Supply_kcal_Data.csv')