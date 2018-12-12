#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:00:04 2018

@author: nenshu
"""
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('revenue_rdexpense.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Fitting Simple Linear Regression to the data set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X, y)

# Visualising the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Simple Linear Regression Model')
plt.xlabel('Revenue(Million Dollars)')
plt.ylabel('R&D Expense(Million Dollars)')
plt.show()

# Print the coeficients and intercept
print('Coefficients: \n', regressor.coef_)
print('Intercept: \n', regressor.intercept_)
