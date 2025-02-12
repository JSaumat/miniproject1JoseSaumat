### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 1

#Imports the required packages
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

# Creates the charts folder to hold the charts created by the program
os.makedirs("charts", exist_ok=True)

#get today's date
today = datetime.now()

#Calculate the date 10 days ago

# Variable that is using time delta from datetime package to get the last 10 days of stock market data
ten_days_ago = today - timedelta(days=14)

# List of all the stocks being used in this mini project
mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

# Dictionary called mydata
mydata = {}

# Cycles through all stock tickers in mytickers list
for ticker in mytickers:

    # Variables using Yahoo Finance to get stock ticker information
    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)

    # List for the last 10 days of data gathered
    last10days = []

    # Cycles through the close dates for the last 10 days
    for date in hist['Close'][:10]:

        # Appends the dates to the list of 10 days for each ticker
        last10days.append(date)

    # Check to make sure we get 10 data points
    if len(last10days) == 10:

        # max_price = np.max(last10days)
        # min_price = np.min(last10days)

        # Uses matplotlib to create the graphs and the information they display
        myarray = np.array(last10days)
        max_price = myarray.max() + (myarray.max()*.05)
        min_price = myarray.min() - (myarray.min()*.05)
        plt.plot(myarray)
        plt.xlabel('Days Ago')
        plt.ylabel('Closing Price')
        plt.axis((9, 0, min_price, max_price))
        plt.title(f"{ticker} Last 10 Closing Prices")
        plt.savefig(f"charts/{ticker}.png")

        #Provides user with the 5 graphs as a pop-up after using terminal
        #plt.show()

    # Message that prints if we do not have 10 days worth of data as required by the specification
    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")