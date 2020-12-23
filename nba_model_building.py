# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:52:05 2020

@author: David
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import r2_score
from sklearn import metrics
import math

df = pd.read_csv('nba_eda.csv')
df_model = df[['CurrentSalary', 'PER', 'VORP','STL', 'G', 'BLK','PTS', 'MP', 'Age',  'WS', 'TRB', 'AST',  'TOV']]

df_test = pd.get_dummies(df_model)
from sklearn.model_selection import train_test_split
X = df_test.drop('CurrentSalary', axis=1)
Y = df_test.CurrentSalary.values

poly = PolynomialFeatures(degree = 2)
x = poly.fit_transform(X)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, Y, test_size = 0.2, random_state = 42)

regressor = LinearRegression(fit_intercept =True, normalize=True)
regressor.fit(x_train, y_train)
pred = regressor.predict(x_test)
r2_score1 = r2_score(y_test, pred)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
lr = RandomForestRegressor(n_estimators=50)
lr.fit(x_train, y_train)
prediction = lr.predict(x_test)
r2_score2 = r2_score(y_test, prediction)

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
reg = AdaBoostRegressor(DecisionTreeRegressor(max_depth =5), n_estimators =500)
adaboost = reg.fit(x_train, y_train)
p = adaboost.predict(x_test)
r2_score3 = r2_score(y_test, p)









