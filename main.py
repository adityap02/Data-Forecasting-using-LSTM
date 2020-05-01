# An object of Flask class is our WSGI application.
from flask import Flask
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import pandas_datareader as web
import math

from tensorflow.keras.models import load_model
import warnings
app = Flask(__name__)
@app.route('/my/<ticker>')

def hello(ticker):
    warnings.filterwarnings("ignore")


    price_history = ticker + ".csv"
    data = web.DataReader(ticker, data_source='yahoo', start='2004-01-01', end='2020-04-24')
    data.to_csv(price_history)
    data = pd.read_csv(price_history, date_parser=True)

    # splitting into training and testing
    data_training = data_training_copy = data[data['Date'] < '2019-04-01'].copy()
    data_test = data[data['Date'] >= '2019-04-01'].copy()

    data_training = data_training.drop(['Date', 'Adj Close'], axis=1)
    scaler = MinMaxScaler()

    def scale_training_data(data_training):
        data_training = scaler.fit_transform(data_training)
        return data_training

    # data_training = scale_training_data(data_training)

    def prep_training_data(data_training):
        X_train = []
        y_train = []

        for i in range(60, data_training.shape[0]):
            X_train.append(data_training[i - 60:i])
            y_train.append(data_training[i, 3])

        X_train, y_train = np.array(X_train), np.array(y_train)
        return X_train, y_train

    # X_train,y_train = prep_training_data(data_training)

    def build_model():
        model = Sequential()

        model.add(LSTM(units=60, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 5)))
        model.add(Dropout(0.2))

        model.add(LSTM(units=60, activation='relu', return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=80, activation='relu', return_sequences=True))
        model.add(Dropout(0.2))

        model.add(LSTM(units=120, activation='relu'))
        model.add(Dropout(0.2))

        model.add(Dense(units=1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    module = ticker + '.h5'

    # model = load_model(module)
    # model = build_model()

    def train_model(model, X_train, y_train):
        model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1, verbose=0)
        trainScore = model.evaluate(X_train, y_train, verbose=0)
        print('MSE :', trainScore)
        print('RMSE : ', math.sqrt(trainScore))
        return model

    # model = train_model(model,X_train,y_train)

    def prep_test_data(data_training_copy, data_test):
        past_60_days = data_training_copy.tail(60)
        df = past_60_days.append(data_test, ignore_index=True)
        df = df.drop(['Date', 'Adj Close'], axis=1)
        inputs = scaler.fit_transform(df)

        X_test = []
        y_test = []

        for i in range(60, inputs.shape[0]):
            X_test.append(inputs[i - 60:i])
            y_test.append(inputs[i, 3])

        X_test, y_test = np.array(X_test), np.array(y_test)
        return X_test, y_test

    # X_test,y_test = prep_test_data(data_training_copy,data_test)

    def make_prediction(X_test, y_test):
        y_pred = model.predict(X_test)
        testScore = model.evaluate(X_test, y_test, verbose=0)
        print("MSE :", testScore)
        return y_pred

    # y_pred = make_prediction(X_test,y_test)

    def inverse_scale(data_test, y_test):
        last_y = data_test.tail()
        last_y = last_y.filter(['Close'])
        last_y = last_y.values.tolist()
        last_y[-1]
        scale2 = last_y[-1] / y_test[-1]
        scale2 = scale2[0]
        return scale2

    # y_pred = inverse_scale(y_pred)
    # y_test = inverse_scale(y_test)

    def plot_results():
        plt.figure(figsize=(7, 5))

        plt.plot(y_test, color='red', label='Real Stock Price')
        plt.plot(y_pred, color='blue', label='Predicted Stock Price')
        plt.title('Stock Price Prediction')
        plt.xlabel('Time')
        plt.ylabel(' Stock Price')
        plt.legend()
        plt.show()

    data_training = scale_training_data(data_training)
    X_train, y_train = prep_training_data(data_training)
    model = load_model(module)
    # model = build_model()
    # model = train_model(model,X_train,y_train)
    X_test, y_test = prep_test_data(data_training_copy, data_test)
    y_pred = make_prediction(X_test, y_test)
    scale2 = inverse_scale(data_test, y_test)
    y_pred = y_pred * scale2
    y_test = y_test * scale2
    line1="Predicted price for the next day is:  " + str(y_pred[-1])+"<br>"
    #print("Predicted price for the next day is:  ", y_pred[-1])

    file = ticker + "_sentiment.csv"

    def sent_analysis(file):
        data = pd.read_csv(file)
        data = data.iloc[:, -1]
        # print(data)
        pos_count = 0
        neg_count = 0
        data = data.values.tolist()
        length = len(data)
        for i in range(length):
            if (data[i] == 'pos'):
                pos_count = pos_count + 1
            elif (data[i] == 'neg'):
                neg_count = neg_count + 1
        p1="============================= <br>"
        p2="sentiment analysis of tweets <br>"
        p3="No of tweets classified as positive: "+str(pos_count)+"<br>"
        p4="No of tweets classified as negative: "+str(neg_count)+"<br>"
        pos_percentage = pos_count * 100 / (neg_count + pos_count)
        neg_percentage = neg_count * 100 / (neg_count + pos_count)
        p5="positive percentage: "+ str(pos_percentage)+"<br>"
        p6="negative percentage: "+str(neg_percentage)+"<br>"
        p7="=============================="
        all_prints=p1+p2+p3+p4+p5+p6+p7
        return all_prints
    line2=sent_analysis(file)
    #plot_results()
    final=line1+line2
    return final

if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
