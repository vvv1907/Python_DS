#!/usr/local/bin/python3

import sys

class Research:
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self):
        with open(self.filename, 'r') as file:
            return(file.read())

def check_arg(filename):
    with open(filename, 'r') as file:
        line = file.readlines()
        if len(line) < 2 or len(line[0].split(',')) != 2:
            raise Exception('Error: wrong file')
        for i in range(1, len(line)):
            if line[i][0:4] != '0,1\n' and line[i][0:4] != '1,0\n' and line[i][0:4] != '1,0' and line[i][0:4] != '1,0':
                raise Exception('Error: wrong file')

if __name__ == '__main__':
    if len (sys.argv) != 2 or check_arg(sys.argv[1]):
        raise Exception('Error: wrong argument')
    print(Research(sys.argv[1]).file_reader())
