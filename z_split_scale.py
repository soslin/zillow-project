

import pandas as pd
from env import host, user, password

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import wrangle_z
from sklearn.preprocessing import StandardScaler


df_z = wrangle_z.wrangle_zillow()
X = df_z.drop(columns=['propertylandusedesc'])
y = pd.DataFrame(df_z.taxvaluedollarcnt)

#1. split_my_data(X, y)
def split_my_data(X,y):
    x_train, x_test, y_train, y_test = train_test_split(X, y, train_size = .8, random_state = 123)
    return x_train, x_test, y_train, y_test
x_train, x_test, y_train, y_test = split_my_data(X,y)



def standard_scaler(x_train, x_test):
    scaler_x_train = StandardScaler(copy=True, with_mean=True, with_std=True)\
                .fit(x_train)
    scaler_x_test = StandardScaler(copy=True, with_mean=True, with_std=True)\
                .fit(x_test)
#scaler.transform
    train_x_scaled_data = pd.DataFrame(scaler_x_train.transform(x_train), columns = x_train.columns.values).set_index([x_train.index.values])
    
    test_x_scaled_data = pd.DataFrame(scaler_x_test.transform(x_test), columns = x_test.columns.values).set_index([x_test.index.values])
    
    return train_x_scaled_data, test_x_scaled_data, scaler_x_train, scaler_x_test
    
train_x_scaled_data, test_x_scaled_data,scaler_x_train, scaler_x_test = standard_scaler(x_train,x_test)



