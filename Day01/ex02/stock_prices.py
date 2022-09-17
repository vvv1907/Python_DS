#!/usr/local/bin/python3

import sys

def data():
    
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    
    return COMPANIES, STOCKS

def stock_prices():
    
    if len(sys.argv) != 2:
        return
    
    name = sys.argv[1].capitalize()
    COMPANIES, STOCKS = data()
    
    if name in COMPANIES:
        print(STOCKS[COMPANIES[name]])
    else:
        print("Unknown company")

if __name__ == '__main__':
    stock_prices()
