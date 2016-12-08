import csv, urllib2, urlparse
from bs4 import BeautifulSoup


def get_boxscore(month, year):
	url = 'http://www.basketball-reference.com/leagues/NBA_%d_games-%s.html' % (year, month)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	rows = soup.findAll('tr')[1:]
	if month == 'april': # take out playoff games
		april = [[td.getText() for td in row.findAll('td')][1:5] for row in rows]
		return april[:april.index([])]
	else:
		return [[td.getText() for td in row.findAll('td')][1:5] for row in rows]

def boxscores_to_file(years):
	games = []
	for year in years:
		months = ['october', 'november', 'december', 'january', 'february', 'march', 'april']
		if year == 2012: # lockout year
			months = months[2:]
		for month in months:
			games += [game + [year] for game in get_boxscore(month, year)]
	with open('games.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows(games)

def player_stats(year, stat_type='per_game'):
	url = 'http://www.basketball-reference.com/leagues/NBA_%d_%s.html' % (year, stat_type)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	rows = soup.findAll('tr')
	header = rows[0]
	rows = rows[1:]
	if stat_type == 'advanced':
		players = [[td.getText() for td in row.findAll('td')] for row in rows]
		players = [player[:18] + player[19:23] + player[24:] for player in players]
		header = [th.getText() for th in header.findAll('th')]
		header = header[1:19] + header[20:24] + header[25:]
	else:
		players = [[td.getText() for td in row.findAll('td')] for row in rows]
		header = [th.getText() for th in header.findAll('th')][1:]
	ids = soup.findAll('td', {'data-append-csv':True})
	players = [[ids[i]['data-append-csv']] + players[i] for i in xrange(len(ids)) if players[i]]
	header = ['ID'] + header
	return header, players

def player_stats_to_file(years, stat_type='per_game'):
	all_stats = []
	for year in years:
		header, stats = player_stats(year, stat_type)
		stats = [player + [year] for player in stats if player]
		all_stats += stats
	header.append('Year')
	with open(stat_type + '.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerows([header] + all_stats)

def player_points(player_id, year):
	url = 'http://www.basketball-reference.com/players/%s/%s/gamelog/%d' % (player_id[0], player_id, year)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	rows = soup.findAll('tr')
	data = [[td.getText() for td in row.findAll('td')] for row in rows]
	points = [int(row[-3]) for row in data if len(row) == 29]
	return points

def team_roster(team, year):
	url = 'http://www.basketball-reference.com/teams/%s/%d.html' % (team.upper(), year)
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')
	div = soup.find('div', {'id' : 'all_roster'})
	ids = div.findAll('td', {'data-append-csv' : True})
	return [ids[i]['data-append-csv'] for i in xrange(len(ids))]

def team_stats(year):
	url = 'http://www.basketball-reference.com/leagues/NBA_%d.html' % year
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html, 'lxml')

if __name__ == '__main__':
	years = [2011, 2012, 2013, 2014, 2015, 2016]
	boxscores_to_file(years)
	player_stats_to_file(years)
	player_stats_to_file(years, 'advanced')
	print player_points('curryst01', 2017)
	print team_roster('gsw', 2016)
print team_stats(2016)