import math

import numpy as np
import pandas as pd

import pandas_datareader as web
from keras.layers import LSTM, Dense
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

#General Description: This program uses an artificial neural network called Long Short term Memory (LSTM)
#to predict the closing stock price of a corporation (Apple Inc.) using the past 60 days stock price

#Get the stock quote and show in graph matplotlib
df=web.DataReader('BRL=X', data_source='yahoo', start='2012-01-01', end='2019-12-17')
print(df)
plt.figure(figsize=(16, 8))
plt.title("Close Price History")
plt.plot(df['Close'])
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
#plt.show()

#Filter an exclusive column - CLOSE PRICE - and put on dataset to be treated as Numpy object
data=df.filter(['Close'])
dataset=data.values

#80% of training numbers
training_data_len = math.ceil(len(dataset) * .8)

#Scale the data between Min=0 and Max=1
scaler=MinMaxScaler(feature_range=(0, 1))
scaled_data=scaler.fit_transform(dataset)
#print(scaled_data)

#Create the training dataset

#Create the scaled training dataset
train_data=scaled_data[0:training_data_len , :]

#Split the data into x_train and y_train dataset
x_train=[]
y_train=[]

for i in range (60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
    if i<=61:
        print(x_train)
        print(y_train)
        print()
        
#Convert x_train and y_train to numpy array

x_train,y_train=np.array(x_train), np.array(y_train)
x_train=np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
#print(x_train.shape)

#build LSTM model
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

#compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
#train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

#Create the testing dataset
#Create a new array containing the scaled values from index 1543 to 2003
test_data=scaled_data[training_data_len - 60:2073, :]

#Create the datasets x_test and y_test
x_test=[]
y_test=dataset[training_data_len:, :]
for i in range(60,len(test_data)):
    x_test.append(test_data[i-60:i, 0])

#Convert the data to a numpy array
x_test=np.array(x_test)
#Reshape for 3 dimensions to LSTM model
x_test=np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#Get the models predicted price values
predictions=model.predict(x_test)
predictions=scaler.inverse_transform(predictions)

#Get the root mean squared error (RMSE)
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(rmse)

#Plot the data
train=data[:training_data_len]
valid=data[training_data_len:]
valid['Predictions']=predictions

#Visualize the data
plt.figure(figsize=(16, 8))
plt.title('Model')
plt.xlabel('Date',fontsize=18)
plt.ylabel('Close Price USD', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'],loc='lower right')
plt.show()

#Show the valid and predicted prices
print(valid)


#How to predict a stock price in a specific date (17-12-2019)
#Get the quote
apple_quote=web.DataReader("BRL=X", data_source='yahoo', start='2012-01-01', end='2019-12-17')
#Create a new dataframe with closing prices
new_df=apple_quote.filter(['Close'])
#Get the last 60 days and convert the dataframe to an array
last_60_days=new_df[-60:].values
#Scale the data to be values between 0 and 1
last_60_days_scaled=scaler.transform(last_60_days)
#Create an empty list and append new scaled items 
X_TEST=[]
X_TEST.append(last_60_days_scaled)
#Convert the dataset into a Numpy array
X_TEST=np.array(X_TEST)
#Reshape the data
X_TEST=np.reshape(X_TEST, (X_TEST.shape[0], X_TEST.shape[1], 1))
#Get the predicted scaled price
pred_price=model.predict(X_TEST)
#Undo the scaler
pred_price=scaler.inverse_transform(pred_price)
print(pred_price)