# Stock Price Prediction and Sentiment Analysis

### Introduction
This GitHub repository contains a Python script for predicting stock prices using a Long Short-Term Memory (LSTM) neural network and performing sentiment analysis on related tweets. The Flask web application allows users to input a stock ticker symbol and receive predictions for the next day's stock price, along with sentiment analysis results based on tweets.

### Dependencies
Make sure you have the following libraries installed:

- Flask
- Numpy
- Matplotlib
- Pandas
- Scikit-learn
- Tensorflow
- Pandas-datareader

You can install them using:
```bash
pip install Flask numpy matplotlib pandas scikit-learn tensorflow pandas-datareader
```

### Usage
1. Run the Flask application:
   ```bash
   python main.py
   ```
   Replace `<filename>` with the name of the Python script containing the provided code.

2. Open your web browser and go to `http://127.0.0.1:5000/my/<ticker>`, replacing `<ticker>` with the stock symbol you want to analyze.For demonstration, i have attached a sample model trained for Tesla Stock (TSLA) : TSLA.h5 and twitter tweets texts in TSLA.csv File.  

3. The web page will display the predicted stock price for the next day and sentiment analysis results for related tweets.

### Code Structure
- The Flask route `/my/<ticker>` triggers the prediction and analysis for the given stock symbol.
- The `web.DataReader` is used to fetch historical stock data from Yahoo Finance.
- The LSTM neural network is implemented using the Keras library for stock price prediction.
- Sentiment analysis is performed on a CSV file containing tweet sentiments.

### Important Notes
- The application is set to run on the local development server. Ensure that you have the necessary dependencies installed before running the script.
- Parts of the code related to data scaling, model training, and result plotting are commented out. Depending on your needs, you may uncomment and use them.

Feel free to explore and modify the code as needed for your projects! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or contribute to the repository.

### Below is the Theoritical Explaination of the Project
## Table of Contents
1. [Introduction](#introduction)
   - [LSTM Neural Network](#lstm-neural-network)
   - [Social Sentiment Analysis](#social-sentiment-analysis)
2. [Literature Survey](#literature-survey)
3. [Methodology](#methodology)
   - [Data Pre-processing](#data-pre-processing)
   - [LSTM Model Training](#lstm-model-training)
   - [Social Sentiment Analysis](#social-sentiment-analysis)
4. [Results & Conclusion](#results--conclusion)
   - [Plotting Results](#plotting-results)
5. [References](#references)

## Introduction
The stock market's performance is closely tied to a country's economic growth. Accurate predictions are valuable for informed decision-making and minimizing trading losses. Conventional statistical analysis is insufficient, given the various factors influencing stock market movements. This project explores the use of LSTM neural networks and social sentiment analysis for improved stock price forecasting.

### LSTM Neural Network
The LSTM architecture is utilized to capture the non-linearities in stock market data. LSTMs are recurrent neural networks designed to process entire sequences of data, addressing the limitations of standard feedforward neural networks.

### Social Sentiment Analysis
Social sentiment, extracted from tweets, is incorporated into the model. Positive or negative news about a company influences stock buying or selling decisions. Sentiment analysis is performed using Textblob, based on the Naïve Bayes Algorithm.

## Literature Survey
Various approaches have been explored for stock market prediction, including technical analysis, news sentiment analysis, linear regression, and neural networks. This project aligns with the understanding that stock markets depend on multiple factors, and efficient machine learning techniques, especially neural networks, can contribute to accurate predictions.

## Methodology
### Data Pre-processing
Data pre-processing involves cleaning, transforming, and reducing noise in the input dataset. This ensures improved data quality for the machine learning model.

### LSTM Model Training
The LSTM neural network is defined, trained using historical price data, and predictions are generated. Model parameters are fine-tuned to reduce mean squared error.

### Social Sentiment Analysis
Text data from tweets undergoes cleansing, tokenization, and enumeration of sentiment. Relevant keywords are used to filter data, and sentiment scores express opinions about a company on social media.

## Results & Conclusion
The LSTM model is refined by adjusting parameters, increasing hidden nodes, adding dropout layers, and extending epochs. The improved model demonstrates reduced mean squared error. The project highlights the complexity and accuracy comparison between Artificial Neural Networks and LSTM.

### Plotting Results
The LSTM model's predicted and real values are plotted, demonstrating the effectiveness of the trained model in capturing stock price trends.

![image](https://github.com/adityap02/Data-Forecasting-using-LSTM/assets/50493250/a957176a-bd38-476c-bcb9-09da44213c3d)
\
