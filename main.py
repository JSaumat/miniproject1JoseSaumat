### INF601 - Advanced Programming in Python
### Jose Saumat
### Mini Project 1

import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}

mytickers.sort()

for ticker in mytickers:

    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticket': ticker, 'dayHigh': result.info['dayHigh']}

    print(f"Ticker: {ticker} \tDay High: {result.info['dayHigh']}")

#aapl = yf.Ticker("AAPL")

#print(aapl.info["dayHigh"])

#get all stock info msft.info
#pprint.pprint(aapl.info)

#get historical market data
#hist = msft.history(period="1mo")

#pprint.pprint(hist)