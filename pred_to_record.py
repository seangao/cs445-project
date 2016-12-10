import pandas as pd
import numpy as np

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