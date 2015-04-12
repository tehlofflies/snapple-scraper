# run with virtualenv
# install requests beautifulsoup

'''produces a large txt file of all the snapple facts'''

import requests
import bs4

base_url = 'http://www.snapple.com/real-facts/list-view/'

def get_snapple_fact():
	outfile = open('facts.txt','w')

	for i in range(1,11):
		url = base_url + str(i)
		response = requests.get(url)
		soup = bs4.BeautifulSoup(response.text)
		d = soup.find_all('p', class_="fact_detail")
		for element in d:
			element = str(element).strip('</p>')
			element = element.strip('<p class="fact_detail">')
			outfile.write((''.join('"' + str(element) + ' lol.", ')))

get_snapple_fact() 