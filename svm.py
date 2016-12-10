from sklearn import svm
import pandas as pd
import numpy as np

Xtrain = np.array(pd.read_csv('csv/x_train.csv', sep=','))
ytrain = np.array(pd.read_csv('csv/y_train.csv', sep=',', header=None))
Xtest = np.array(pd.read_csv('csv/x_test.csv', sep=','))
ytest = np.array(pd.read_csv('csv/y_test.csv', sep=',', header=None))

clf = svm.SVC(C = 0.5, kernel='linear')
clf.fit(Xtrain, ytrain)

p = clf.predict(Xtest)

print np.sum(p == np.ravel(ytest)) / (len(p) + 0.0)