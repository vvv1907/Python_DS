#!/usr/bin/env python3

import sys
import timeit

def get_with_for_loop():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	new_emails = []
	for email in emails:
		if email.endswith('@gmail.com'):
			new_emails.append(email)
	return new_emails

def get_with_list_comprehension():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	new_emails = [email for email in emails if email.endswith('@gmail.com')]
	return new_emails

def get_with_map():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	new_emails = map(lambda x: x if x.endswith('@gmail.com') else None, emails)
	return new_emails

def get_with_filter():
	emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5
	new_emails = filter(lambda x: x if x.endswith('@gmail.com') else None, emails)
	return new_emails

def my_time(func_name, num):
	times = timeit.timeit(func_name, number = num)
	print(times)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise Exception('Error: wrong arguments number')
	if sys.argv[1] == 'loop':
		arg = get_with_for_loop
	elif sys.argv[1] == 'list_comprehension':
		arg = get_with_list_comprehension
	elif sys.argv[1] == 'map':
		arg = get_with_map
	elif sys.argv[1] == 'filter':
		arg = get_with_filter
	else:
		raise Exception('Error: wrong function name')
	my_time(arg, int(sys.argv[2]))
