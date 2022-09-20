#!/usr/bin/env python3

import os

def main():
    if os.getenv("VIRTUAL_ENV") is None:
        print('You are not in the Virtual Environment')
    else: 
        environ = os.getenv("VIRTUAL_ENV")
        if environ.endswith('hcolumbu_02'):
            print("This is ex02 enviroment")
            os.system("pip3 install beautifulsoup4 PyTest")
            os.system("pip3 freeze > requirements.txt")
        else:
            print('Virtual Environment is different')

if __name__ == '__main__':
 main()
 