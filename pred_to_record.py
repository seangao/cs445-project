import pandas as pd
import numpy as np
import csv

colors = {'Atlanta Hawks': '#E03A3E',
	'Boston Celtics': '#008348',
	'Brooklyn Nets': '#000000',
	'Charlotte Hornets': '#1D1160',
	'Chicago Bulls': '#CE1141',
	'Cleveland Cavaliers': '#860038',
	'Dallas Mavericks': '#20385B',
	'Denver Nuggets': '#4FA8FF',
	'Detroit Pistons': '#001F70',
	'Golden State Warriors': '#006BB6',
	'Houston Rockets': '#CE1141',
	'Indiana Pacers': '#00275D',
	'Los Angeles Clippers': '#ED174C',
	'Los Angeles Lakers': '#552582',
	'Memphis Grizzlies': '#23375B',
	'Miami Heat': '#98002E',
	'Milwaukee Bucks': '#00471B',
	'Minnesota Timberwolves': '#005083',
	'New Orleans Pelicans': '#002B5C',
	'New York Knicks': '#F58426',
	'Oklahoma City Thunder': '#007DC3',
	'Orlando Magic': '#007DC5',
	'Philadelphia 76ers': '#006BB6',
	'Phoenix Suns': '#1D1160',
	'Portland Trail Blazers': '#F0163A',
	'Sacramento Kings': '#724C9F',
	'San Antonio Spurs': '#000000',
	'Toronto Raptors': '#CE1141',
	'Utah Jazz': '#002B5C',
	'Washington Wizards': '#002566'}

def pred_to_record(pred):
	results = pd.read_csv('games_test.csv', header=None)
	teams = pd.read_csv('teams.csv', header=None)

	if len(pred) != 2*len(results):
		print 'Length mismatch'
		return

	records = {}
	for team in teams[0]:
		records[team] = [0, 0]

	for i in xrange(len(results)):
		records[results.iloc[i, 0]][0] += pred[2*i]
		records[results.iloc[i, 0]][1] += 1-pred[2*i]
		records[results.iloc[i, 2]][0] += pred[2*i+1]
		records[results.iloc[i, 2]][1] += 1-pred[2*i+1]

	return records

def rms(pred):
	actual = list(pd.read_csv('csv/y_test.csv', header=None)[0])

	pred_record = pred_to_record(pred)
	actual_record = pred_to_record(actual)

	RMS = 0
	for team in pred_record:
		RMS += (pred_record[team][0]-actual_record[team][0])**2
	return (RMS/len(pred_record))**.5

def rms_round(pred):
	actual = list(pd.read_csv('csv/y_test.csv', header=None)[0])

	pred_record = pred_to_record(pred)
	actual_record = pred_to_record(actual)

	RMS = 0
	for team in pred_record:
		RMS += (round(pred_record[team][0])-actual_record[team][0])**2
	return (RMS/len(pred_record))**.5

def to_csv(pred, name):
	all_games = pd.read_csv('csv/games.csv', header=None)

	wins = {}
	games = all_games[all_games[4] == 2016]
	for index, game in games.iterrows():
	    if game[3] > game[1]:
	        if game[2] not in wins:
	            wins[game[2]] = 1
	        else:
	            wins[game[2]] += 1
	    else:
	        if game[0] not in wins:
	            wins[game[0]] = 1
	        else:
	            wins[game[0]] += 1

	pr_vs_actual = [[i, int(round(pred[i][0])), wins[i], colors[i]] for i in pred]
	with open('csv/%s.csv' % name, 'w') as f:
		writer = csv.writer(f)
		writer.writerows(pr_vs_actual)