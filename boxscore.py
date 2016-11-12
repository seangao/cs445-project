import csv, urllib2
from bs4 import BeautifulSoup


def get_games(month, year):
	url = 'http://www.basketball-reference.com/leagues/NBA_%d_games-%s.html' % (year, month)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	rows = soup.findAll('tr')[1:]
	if month == 'april':
		april = [[td.getText() for td in row.findAll('td')][1:5] for row in rows]
		return april[:april.index([])]
	else:
		return [[td.getText() for td in row.findAll('td')][1:5] for row in rows]

def games_to_file(years):
	games = []
	for year in years:
		months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
		if year == 2012: # lockout year
			months = months[2:]
		for month in months:
			games += [game + [year] for game in get_games(month, year)]
	with open('games.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(games)

games_to_file([2012, 2013, 2014, 2015, 2016])
