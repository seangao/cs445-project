import numpy as np
import pandas as pd

def main():
    games_train = pd.read_csv('games_train.csv', header=None)
    elos = train_elos(games_train)
    dump_elos(elos)
    games_test = pd.read_csv('games_test.csv', header=None)
    pred = test_elos(elos, games_test)
    interpret_predictions(pred)

def train_elos(data, K=32):
    elos = {}
    for team in set(data[0]).union(set(data[2])):
        elos[team] = 1200.0
    
    for i in xrange(len(data)):
        game = data.iloc[i,]
        team1 = game[0]
        rating1 = elos[team1]
        team2 = game[2]
        rating2 = elos[team2]
        t_rating1 = 10**(rating1/400.0)
        t_rating2 = 10**(rating2/400.0)
        e_score1 = t_rating1/(t_rating1+t_rating2)
        e_score2 = t_rating2/(t_rating1+t_rating2)
        if game[1] > game[3]:
            s1 = 1
            s2 = 0
        else:
            s1 = 0
            s2 = 1
        u_rating1 = rating1 + K*(s1-e_score1)
        u_rating2 = rating2 + K*(s2-e_score2)
        elos[team1] = u_rating1
        elos[team2] = u_rating2
    
    return elos

def dump_elos(elos):
    import operator
    sorted_elos = sorted(elos.items(), key=operator.itemgetter(1))
    print sorted_elos[::-1]

def test_elos(model, data):
    data["TrueWinner"] = ""
    data["TrueLoser"] = ""
    data["PredWinner"] = ""
    data["PredLoser"] = ""
    for i in xrange(len(data)):
        game = data.iloc[i,]
        if game[1] > game[3]:
            data.iloc[i,5] = game[0]
            data.iloc[i,6] = game[2]
        else:
            data.iloc[i,5] = game[2]
            data.iloc[i,6] = game[0]
        if model[game[0]] > model[game[2]]:
            data.iloc[i,7] = game[0]
            data.iloc[i,8] = game[2]
        else:
            data.iloc[i,7] = game[2]
            data.iloc[i,8] = game[0]
    return data

def interpret_predictions(pred):
    result = {}
    for team in set(pred[0]).union(set(pred[2])):
        result[team] = {'predicted':{'win':0, 'loss':0}, 'actual':{'win':0, 'loss':0}}

    for i in xrange(len(pred)):
        game = pred.iloc[i,]
        result[game["PredWinner"]]['predicted']['win'] += 1
        result[game["PredLoser"]]['predicted']['loss'] += 1
        result[game["TrueWinner"]]['actual']['win'] += 1
        result[game["TrueLoser"]]['actual']['loss'] += 1

    print result
    print 'Prediction Accuracy:', (sum(pred["TrueWinner"] == pred["PredWinner"])+0.0)/len(pred)

if __name__ == "__main__":
    main()