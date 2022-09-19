#!/usr/local/bin/python3

import sys

class Research:
    def __init__(self, filename):
        self.filename = filename

    def file_reader(self, has_header = True):
        with open(self.filename, 'r') as file:
            line = file.readlines()
            if line[0] == '0,1\n' or line[0] == '1,0\n':
                self.has_header = False
            start = 0
            if has_header == True:
                start = 1
            list_lists = []
            for i in range(start, len(line)):
                list_i = [int(line[i][0])]
                list_i.append(int(line[i][2]))
                list_lists.append(list_i)
            return(list_lists)

    class Calculations:
        def counts(self, list_lists):
            heads = 0
            tails = 0
            for i in range(len(list_lists)):
                if list_lists[i][0] == 1:
                    heads += 1
                else:
                    tails += 1
            return(heads, tails)

        def fractions(self, list_counts):
            sum_counts = list_counts[0] + list_counts[1]
            return(list_counts[0] / sum_counts * 100, list_counts[1] / sum_counts * 100)


def check_arg(filename):
    with open(filename, 'r') as file:
        line = file.readlines()
        if len(line) == 0 or (len(line) == 1 and (line[0] != '0,1\n' and line[0] != '1,0\n')):
            raise Exception('Error: wrong file')
        if len(line) > 1:
            for i in range(1, len(line)):
                if line[i][0:4] != '0,1\n' and line[i][0:4] != '1,0\n' and line[i][0:4] != '1,0' and line[i][0:4] != '1,0':
                    raise Exception('Error: wrong file')

if __name__ == '__main__':
    if len (sys.argv) != 2 or check_arg(sys.argv[1]):
        raise Exception('Error: wrong argument')
    research = Research(sys.argv[1])
    data = research.file_reader()
    print(data)
    calculations = research.Calculations()
    counts = calculations.counts(data)
    print(counts[0], counts[1])
    fractions = calculations.fractions(counts)
    print(fractions[0], fractions[1])
