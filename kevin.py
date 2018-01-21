import pandas as pd
import numpy as np
from clean import returnClean

def kevin(n, SOC_NAME, FULL_TIME_POSITION, PREVAILING_WAGE, WORKSITE, lon, lat):

    h1b_data = returnClean(n, n)

    #Train/Test Split:
    train = h1b_data
    
    #Dropping JobTitle
    X = train.drop(['CASE_STATUS','JOB_TITLE'], axis=1)
    Y = train['CASE_STATUS']

    import sklearn
    from sklearn.neighbors import KNeighborsClassifier

    clf = KNeighborsClassifier()
    clf.fit(X, Y)

    l = [[SOC_NAME, FULL_TIME_POSITION, PREVAILING_WAGE, WORKSITE, lon, lat]]
    y = clf.predict(l)

    return y[0]
