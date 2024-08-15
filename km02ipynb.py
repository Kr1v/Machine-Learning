# -*- coding: utf-8 -*-
"""km02ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CN6vKhwUEMv1Q_oqO8UFPSY3DyLgOAnO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the iris dataset from sklearn
from sklearn.datasets import load_iris
iris = load_iris()

df_x = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df_y = pd.DataFrame(data=iris.target, columns=['species'])

df_x.head()

df_y.head()

df_y['species'].value_counts()

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=0)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

# standardize the data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# train logistic regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train.values.ravel())

model.score(x_train, y_train)

# evaluate the model
y_pred = model.predict(x_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(model.score(x_test, y_test)))