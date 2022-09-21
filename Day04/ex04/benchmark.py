#!/usr/bin/env python3

import timeit
from random import randint
from collections import Counter

def my_function(lst):
    dict_all = {}
    for element in lst:
        if element not in dict_all:
            dict_all[element] = 1
        else:
            dict_all[element] += 1
    return dict_all

def my_top(lst):
    my_dict = my_function(lst)
    sorted_list = sorted(my_dict.items(), key=lambda item: -int(item[1]))
    top_list = sorted_list[:10]
    my_top_dict = dict((x, y) for x, y in top_list)
    return my_top_dict

def counter_dict(lst):
    return dict(Counter(lst))

def counter_top(lst):
    return Counter(lst).most_common(10)

def benchmark(lst):
    print('my function:', timeit.timeit(f'my_function({lst})', number=1,
									setup='from __main__ import my_function'))
    print('Counter:', timeit.timeit(f'counter_dict({lst})', number=1,
									setup='from __main__ import counter_dict'))
    print('my top:', timeit.timeit(f'my_top({lst})', number=1,
									setup='from __main__ import my_top'))
    print('Counter\'s top:', timeit.timeit(f'counter_top({lst})', number=1,
									setup='from __main__ import counter_top'))
    
if __name__ == '__main__':
	rand_list = [randint(0, 100) for i in range(10 ** 6)]
	benchmark(rand_list)
