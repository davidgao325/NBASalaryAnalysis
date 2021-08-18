# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:21:38 2020

@author: David
"""
### Data Cleaning
# Import the csv file into a dataframe
# Drop the unnamed column
import pandas as pd
import numpy as np
df = pd.read_csv('merged_dataset2.csv')
df.drop(["Unnamed: 0"], axis=1, inplace=True)
df.drop(["Unnamed: 19"], axis=1, inplace=True)
df.drop(["Unnamed: 24"], axis=1, inplace=True)

#Remove the empty rows and any duplicates rows
# Keep the first copy of duplicated rows
df.drop_duplicates(keep=False,inplace=True)
result = df.drop_duplicates(subset=['Player'], keep='first')
result = result.fillna('0')

# Remove the dollar sign and commas in the salary columns
result = result.apply(lambda x: x.str.replace('$', ''))
result = result.apply(lambda x: x.str.replace(',', ''))

col1 = 'AST'
col2 = 'BLK'
result = result[[col1 if col == col2 else col2 if col == col1 else col for col in result.columns]]


cleanedup_data = result.to_csv("cleanedup_data.csv")