import os, csv
import yfinance as yf
import pandas
def snapshot():
    with open('datasets/symbols6.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[1]
            Name = line.split(",")[0]
           #            data = yf.download(symbol, start="2020-01-01", end="2021-01-07", threads = True)
            data = yf.download(symbol, period="1mo", threads = True)
            data.to_csv('datasets/daily1/{}.csv'.format(Name))

    return {
        "code": "success"
    }
snapshot()