

import pandas as pd
from env import host, user, password

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
import wrangle_z
from sklearn.preprocessing import StandardScaler


df_z = wrangle_z.wrangle_zillow()
X = df_z.drop(columns=['Property Description'])
y = pd.DataFrame(df_z['Tax Appraised Value'])

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


#uniform_scaler()
def uniform_scaler(x_train, x_test):
    u_scaler_x_train = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(x_train[['monthly_charges', 'tenure']])
   
    u_train_x_scaled = pd.DataFrame(u_scaler_x_train.transform(x_train), columns = x_train.columns.values).set_index([x_train.index.values])
    u_test_x_scaled = pd.DataFrame(u_scaler_x_train.transform(x_test), columns = x_test.columns.values).set_index([x_test.index.values])
    
    return u_train_x_scaled, u_test_x_scaled

u_train_x_scaled, u_test_x_scaled = uniform_scaler(x_train, x_test)



#gaussian_scaler()
def gaussian_scaler(x_train, x_test):
    g_x_train_scaler =PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(x_train[['monthly_charges', 'tenure']])
    
    g_x_train_scaled = pd.DataFrame(g_x_train_scaler.transform(x_train), columns = x_train.columns.values).set_index([x_train.index.values])
    g_x_test_scaled = pd.DataFrame(g_x_train_scaler.transform(x_test), columns = x_test.columns.values).set_index([x_test.index.values])
    
    return g_x_train_scaled, g_x_test_scaled

g_x_train_scaled, g_x_test_scaled = gaussian_scaler(x_train, x_test)

#iqr_robust_scaler()
def iqr_robust_scaler (x_train, x_test):
    iqr_x_train_scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(x_train[['monthly_charges', 'tenure']])

    iqr_x_train_scaled = pd.DataFrame(iqr_x_train_scaler.transform(x_train), columns = x_train.columns.values).set_index([x_train.index.values])
    iqr_x_test_scaled = pd.DataFrame(iqr_x_train_scaler.transform(x_test), columns = x_test.columns.values).set_index([x_test.index.values])
    
    return iqr_x_train_scaled, iqr_x_test_scaled

iqr_x_train_scaled, iqr_x_test_scaled = iqr_robust_scaler (x_train, x_test)