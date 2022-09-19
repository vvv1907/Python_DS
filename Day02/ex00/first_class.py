#!/usr/local/bin/python3

class Must_read:
    with open('data.csv', 'r') as file:
        print(file.read())

if __name__ == '__main__':
    Must_read()
