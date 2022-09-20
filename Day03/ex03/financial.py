#!/usr/bin/env python3

import sys
import time
import requests
from bs4 import BeautifulSoup

def parse_info():
	time.sleep(5)

	url = f'https://finance.yahoo.com/quote/{sys.argv[1]}/financials'
	website = requests.get(url, headers={'User-Agent' : 'Custom user agent'})

	if website.status_code != 200:
		raise Exception ('Error: page is not found')

	soup = BeautifulSoup(website.text, 'html.parser')
	elements = soup.find_all('div', attrs={'data-test' : 'fin-row'})
	for i in elements:
		if i.find('div', attrs={'title' : sys.argv[2]}) is not None:
			cols = i.find_all('div', attrs={'data-test' : 'fin-col'})
			my_list = [col.text for col in cols]
			return tuple([sys.argv[2], *my_list])
	raise Exception ('Error: statement name is not found')

if __name__ == '__main__':
	if len(sys.argv) != 3:
		raise Exception('Error: wrong num of arg')
	
	info = parse_info()
	if info is None:
		raise Exception('Error: invalid info')
	print(info)
 