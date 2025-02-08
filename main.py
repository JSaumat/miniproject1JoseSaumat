### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 1

import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

#get today's date
today = datetime.now()

#Calculate the date 10 days ago

ten_days_ago = today - timedelta(days=14)

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}

for ticker in mytickers:

    result = yf.Ticker(ticker)
    hist = result.history(start=ten_days_ago, end=today)

    last10days = []

    for date in hist['Close'][:10]:

        last10days.append(date)

    if len(last10days) == 10:

        # max_price = np.max(last10days)
        # min_price = np.min(last10days)

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

    else:
        print(f"Do not have 10 days of data. Only have {len(last10days)} days.")