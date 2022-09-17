#!/usr/local/bin/python3

import sys

def find_element(elem):
    
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }
    
    tickers = {value: key for key, value in companies.items()}
    
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    
    words = sys.argv[1].replace(' ', '').split(',')
    
    for word in words:
        if not word:
            print('')
            return
    
    for word in words:
        if word.upper() in stocks:
            print("%s is a ticker symbol for %s"
                % (word.upper(), tickers[word.upper()]))
        elif word.capitalize() in companies:
            print("%s stock price is %s"
                % (word.capitalize(), stocks[companies[word.capitalize()]]))
        else:
            print("%s is an unknown company or an unknown ticker symbol"
                % (word))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        find_element(sys.argv[1])
