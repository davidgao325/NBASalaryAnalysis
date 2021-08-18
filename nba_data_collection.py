# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:52:42 2020

@author: David
"""
### Data Scraping

import pandas as pd

# Take the html website and convert it into a single dataframe
# Change the name of columns that don't have a name, to make it 
# easier to merge data together at a common index and will be used
# In the data cleaning portion

url1 = 'https://www.basketball-reference.com/contracts/players.html'
df1= pd.read_html(url1, header=0)[0]
df1.rename(columns={"Unnamed: 1": "Player", 
                     "Salary":"CurrentSalary",
                    "Salary.1":"UpcomingSalary"}, inplace=True)
# Remove duplicated header information at the top of the dataframe

df1.drop([0], axis=0, inplace=True)
df1.drop(["Unnamed: 0", "Unnamed: 2", "Salary.2", "Salary.3",
          "Salary.4", "Salary.5",  "Unnamed: 9", "Unnamed: 10"], 
         axis=1, inplace=True)
#Convert the html website into a signle dataframe

url2 = 'https://www.basketball-reference.com/leagues/NBA_2021_per_game.html'
df2 = pd.read_html(url2, header=0)[0]

# Remove features that won't be used for testing later on

df2.drop(["Rk"], axis=1, inplace=True)
df2.drop(df2.iloc[:, 1:2], inplace = True, axis = 1)
df2.drop(["GS"], axis=1, inplace=True)
df2.drop(["FG"], axis=1, inplace=True)
df2.drop(df2.loc[:, 'FGA':'3P'], axis = 1, inplace=True)
df2.drop(df2.loc[:, '2P':'DRB'].columns, axis = 1, inplace=True)
df2.drop(['PF'], axis = 1, inplace=True) 

url3 = 'https://www.basketball-reference.com/leagues/NBA_2021_advanced.html'
df3 = pd.read_html(url3, header=0)[0]
df3.drop(df3.loc[:, 'Pos':'MP'].columns, axis = 1, inplace=True)
df3.drop(df3.loc[:, '3PAr':'USG%'].columns, axis = 1, inplace=True)
df3.drop(['WS/48'], axis = 1, inplace=True)
df3.drop(["Rk"], axis=1, inplace=True)




# Combine the dataframes into one at the index "Player", since the player
#index is common in all dataframes
# Convert the dataframe into a csv file to be accessed for data cleaning

merged_dataset = pd.merge(df1,df2, on="Player")
merged_dataset_2 = pd.merge(merged_dataset, df3, on="Player")
merged_dataset_2.to_csv("merged_dataset2.csv") 



    
