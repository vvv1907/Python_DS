#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import pytest

def parse_info(ar1, ar2):

	url = f'https://finance.yahoo.com/quote/{ar1}/financials'
	headers={'User-Agent': 'Custom user agent'}
	website = requests.get(url, headers=headers)

	if website.status_code != 200:
		raise Exception ('Error: page is not found')

	soup = BeautifulSoup(website.text, 'html.parser')
	elements = soup.find_all('div', attrs={'data-test' : 'fin-row'})
	for i in elements:
		if i.find('div', attrs={'title' : ar2}) is not None:
			cols = i.find_all('div', attrs={'data-test' : 'fin-col'})
			my_list = [col.text for col in cols]
			return tuple([ar2, *my_list])
	return('Ticker is not found')

def main():
	if len(sys.argv) != 3:
		raise Exception('Error: wrong num of arg')
	try:
		print(parse_info(sys.argv[1], sys.argv[2]))
	except:
		print('Error: invalid info')

def test_total():
	result = parse_info('MSFT', 'Total Revenue')
	assert result[0] == 'Total Revenue'

def test_tuple():
	result = parse_info('MSFT', 'Total Revenue')
	assert type(result) is tuple

def test_exception():
	result = parse_info('RTFM', 'Total Revenue')
	assert result == 'Ticker is not found'

if __name__ == '__main__':
	main()
	test_total()
	test_tuple()
	test_exception()
 