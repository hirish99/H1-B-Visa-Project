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

##############################################################################################################################
#Renames SOC_NAME to numerical inputs
h1b_data = h1b_data.head(1500) #Working with head because this csv is ginormous
SOC_vals = h1b_data.SOC_NAME.unique()
SOC_vals = list(SOC_vals)
dict_SOC = {}
for i in range(len(SOC_vals)):
	dict_SOC[SOC_vals[i]]=i
h1b_data.replace(dict_SOC,inplace=True)

#Rename Location to numerical inputs

state_list = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming','District of Columbia','Puerto Rico','Guam','American Samoa','U.S. Virgin Islands','Northern Mariana Islands']
states_dict = {}

for i in range(len(states_dict)):
    states_dict[state_list[i]]=i
for z in range(len(state_list)):
    h1b_data.WORKSITE = h1b_data.WORKSITE.apply(lambda x: state_list[z].upper() if state_list[z].upper() in x else x)


#normalize wage data
norm_wage = (h1b_data["PREVAILING_WAGE"] - h1b_data["PREVAILING_WAGE"].mean()) / (h1b_data["PREVAILING_WAGE"].max() - h1b_data["PREVAILING_WAGE"].min())
h1b_data
