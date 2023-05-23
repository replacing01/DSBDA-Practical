# -*- coding: utf-8 -*-
"""DSBDA9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ri5VdosOlWZZgR5rPNCu4s6cWHvYGOKU
"""

import pandas as pd
import numpy as np
import seaborn as sns

df = sns.load_dataset('titanic')

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df['embarked'].value_counts()

df['embarked'].fillna('S',inplace=True)

df.fillna(method='ffill',inplace=True)

df.isnull().sum()

df.fillna(method='bfill',inplace=True)

df.isnull().sum()

sns.boxplot(x='sex',y='age',hue='survived',data=df)

