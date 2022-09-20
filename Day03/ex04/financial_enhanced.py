#!/usr/bin/env python3

import sys
import httpx
from bs4 import BeautifulSoup

def parse_info():

	url = f'https://finance.yahoo.com/quote/{sys.argv[1]}/financials'
	headers={'User-Agent': 'Custom user agent'}
	try:
		website = httpx.get(url, headers=headers)
	except:
		print('\nWrong URL\n')

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
	try:
		print(parse_info())
	except:
		print('Error: invalid info')	
 
############################

	# import cProfile
	# from pstats import Stats
	# from pstats import SortKey

	# pr = cProfile.Profile()
	# pr.enable()

	# parse_info()

	# pr.disable()
	# stats = Stats(pr)
	# stats.sort_stats(SortKey.CUMULATIVE).print_stats(5)
