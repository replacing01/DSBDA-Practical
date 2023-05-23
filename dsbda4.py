# -*- coding: utf-8 -*-
"""DSBDA4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UNG4pDH4E8eU6KYI19Rpo7ntvdCDqCWi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/housing.csv')

df.info()

df = df.rename(columns = {'MEDV':'price'})

df.info()

df.isnull().sum()

x = df.drop(['price'], axis=1)

y = df['price']

y











"""EXPLORATARY DATA ANALYSIS (EDA)"""

plt.figure(figsize=(12,8))
sns.boxplot(data = df)



# splitting of to x_train, x_test, y_train, y_test
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)

# MODEL SELECTION
from sklearn.linear_model import LinearRegression

model=LinearRegression()

# MODEL TRAINING
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

y_pred

y_test

len(y_pred)

len(y_test)







# MODEL EVALUATION WITH EVALUATION METRICS LIKE MAE, MSE, RSQUARE

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

error1 = mean_absolute_error(y_test, y_pred)

error1

error2 = mean_squared_error(y_test, y_pred)

error2

error3 = r2_score(y_test, y_pred)

error3

# VISUALIZATION BY MATPLOTLIB AND SEABORN

plt.scatter(y_test,y_pred,c='lightgreen',marker='s',label='Test data') 
plt.scatter(y_test,y_test,c="red",marker='s',label='Test data')
plt.xlabel('y_test')
plt.ylabel('Predictedvalue')
plt.title("True value vs Predicted value")



