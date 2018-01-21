import pandas as pd
import numpy as np
from clean import returnClean

n = 1000
m = 1000
p = 0.75

h1b_data = returnClean(n, m)

#Train/Test Split:
train = h1b_data.sample(frac=p, random_state=200)
test = h1b_data.drop(train.index)
test.to_csv('test')

#Dropping JobTitle
X = train.drop(['CASE_STATUS','JOB_TITLE'], axis=1)
Y = train['CASE_STATUS']


import sklearn
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()
clf.fit(X, Y)

result = test
result['OUTPUT'] = clf.predict(test.drop(['CASE_STATUS','JOB_TITLE'], axis=1))

result['DIFFERENCE'] = result['OUTPUT'] - result['CASE_STATUS']
print('KNeighbors Percentage Incorrect: ', result['DIFFERENCE'].sum()/(100*len(result.columns)))
result.to_csv('OUTPUT.CSV')

