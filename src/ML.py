import pandas as pd
import numpy as np
from clean import returnClean

h1b_data = returnClean()

#Train/Test Split:
train = h1b_data.sample(frac=0.8, random_state=200)
test = h1b_data.drop(train.index)

X = h1b_data.drop('CASE_STATUS', axis=1)
Y = h1b_data['CASE_STATUS']

import sklearn
from sklearn.svm import LinearSVC

clf = LinearSVC()
clf.fit(X, Y)

result = test
result['OUTPUT'] = clf.predict(test.drop('CASE_STATUS', axis=1))
result.drop(['EMPLOYER_NAME', 'SOC_NAME', 'JOB_TITLE', 'FULL_TIME_POSITION', 'PREVAILING_WAGE', 'YEAR', 'WORKSITE'], axis=1, inplace=True)
result.to_csv('OUTPUT.CSV')
