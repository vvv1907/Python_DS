#!/usr/bin/env python3

import sys
import timeit
from functools import reduce

def sum_with_for_loop(n):
    sum_square = 0
    for i in range(1, n + 1):
        sum_square += i * i
        return sum_square

def sum_with_reduce(n):
    sum_square = reduce(lambda y, x: y + x ** 2, range(1, n + 1))
    return sum_square

def benchmark(command, n_of_calls, n_for_sum):
    SETUP_CODE = f'from __main__ import {command}'
    TEST_CODE = f'{command}({n_for_sum})'
    times = timeit.timeit(setup = SETUP_CODE, stmt = TEST_CODE, number = n_of_calls)
    print(times)

if __name__ == '__main__':
	if len(sys.argv) != 4:
		raise Exception('Error: wrong arguments number')
	if sys.argv[1] == 'loop':
		command = 'sum_with_for_loop'
	elif sys.argv[1] == 'reduce':
		command = 'sum_with_reduce'
	else:
		raise Exception('Error: wrong function name')
	benchmark(command, int(sys.argv[2]), int(sys.argv[3]))
