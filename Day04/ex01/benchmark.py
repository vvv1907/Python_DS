#!/usr/bin/env python3

import timeit

def get_with_for_loop(emails):
	new_emails = []
	for email in emails:
		if email.endswith('@gmail.com'):
			new_emails.append(email)
	return new_emails

def get_with_list_comprehension(emails):
	new_emails = [email for email in emails if email.endswith('@gmail.com')]
	return new_emails

def get_with_map(emails):
    new_emails = map(lambda x: x if x.endswith('@gmail.com') else None, emails)
    return new_emails

def time_loop():
	SETUP_CODE = 'from __main__ import get_with_for_loop'
	ITERATIONS = 9 * 10 ** 7
	times = timeit.timeit(setup = SETUP_CODE, number = ITERATIONS)
	return times

def time_comprehension():
	SETUP_CODE = 'from __main__ import get_with_list_comprehension'
	ITERATIONS = 9 * 10 ** 7
	times = timeit.timeit(setup = SETUP_CODE, number = ITERATIONS)
	return times

def time_map():
	SETUP_CODE = 'from __main__ import get_with_map'
	ITERATIONS = 9 * 10 ** 7
	times = timeit.timeit(setup = SETUP_CODE, number = ITERATIONS)
	return times

if __name__ == '__main__':
    
    emails = ['john@gmail.com', 'james@gmail.com',
			'alice@yahoo.com', 'anna@live.com', 
			'philipp@gmail.com'] * 5
    time_1 = time_loop()
    time_2 = time_comprehension()
    time_3 = time_map()

    times = (time_1, time_2, time_3)
    times = tuple(sorted(times))
    
    if (times[0] == time_1):
        print('it is better to use a loop')
    elif (times[0] == time_2):
        print('it is better to use a list comprehension')
    elif (times[0] == time_3):
        print('it is better to use a map')
    
    print(f'{times[0]} vs {times[1]} vs {times[2]}')
