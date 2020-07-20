import math

import numpy as np
import pandas as pd

import pandas_datareader as web
'''from keras.layers import LSTM, Dense
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler'''
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#Get the stock quote
df=web.DataReader('POMO3.SA', data_source='yahoo', start='2012-01-01', end='2020-07-19')
print(df)
plt.figure(figsize=(16,8))
plt.title("Close Price History")
plt.plot(df['Close'])
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()
