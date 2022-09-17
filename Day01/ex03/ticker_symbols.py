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
    
    inv_COMPANIES = {value: key for key, value in COMPANIES.items()}
    
    return inv_COMPANIES, STOCKS

def search():
    
    if len(sys.argv) != 2:
        return
    
    name = sys.argv[1].upper()
    COMPANIES, STOCKS = data()
    
    if name in STOCKS:
        print(COMPANIES[name], STOCKS[name])
    else:
        print("Unknown company")

if __name__ == '__main__':
    search()
