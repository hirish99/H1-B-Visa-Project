import pandas as pd
import numpy as np
from clean import returnClean


h1b_data = returnClean()

#Train/Test Split:
train = h1b_data.sample(frac=0.25, random_state=200)
test = h1b_data.drop(train.index)
test.to_csv('test')

#Dropping JObTitle
X = train.drop(['CASE_STATUS','JOB_TITLE'], axis=1)
Y = train['CASE_STATUS']


import sklearn
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier()
clf.fit(X, Y)

result = test
result['OUTPUT'] = clf.predict(test.drop(['CASE_STATUS','JOB_TITLE'], axis=1))
result.to_csv('OUTPUT.CSV')
result['DIFFERENCE'] = result['OUTPUT'] - result['CASE_STATUS']
print('KNeighbors Percentage Correct: ', result['CASE_STATUS'].sum()/68.87)
