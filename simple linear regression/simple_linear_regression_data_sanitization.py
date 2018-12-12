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
dataset = pd.read_csv('revenue_rdexpense_need-sanitization.csv')

# Sanitize the data
columns = dataset.columns

# Remove the dollar signs and the commas
for i in range(0, 2):
    dataset[columns[i]] = dataset[columns[i]].str.replace(',', '')
    dataset[columns[i]] = dataset[columns[i]].str.replace('$', '')

dataset.sort_values(columns[0])

X = dataset.iloc[:, 0:1].values
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
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Revenue')
plt.ylabel('R&D Expense')
plt.show()
