def returnClean(n, m):
    import pandas as pd
    h1b_data = pd.read_csv("./h1b_kaggle.csv")

    df = h1b_data
    df = df.loc[df['CASE_STATUS'] == 'DENIED']
    df = df.tail(m)
    
    #TEMP: SHORTENED DATA:
    h1b_data = h1b_data.head(n)
    h1b_data = pd.concat([h1b_data, df])
    h1b_data.replace({'N':0, 'Y':1}, axis=1, inplace=True)
    h1b_data.drop(['Unnamed: 0','YEAR','EMPLOYER_NAME'], axis=1, inplace=True)


    #Renaming SOC_NAME
    SOC_vals = list(h1b_data.SOC_NAME.unique())
    numbers = list(range(len(SOC_vals)))
    SOC_vals_dict = dict(zip(SOC_vals, numbers))


    #Renaming CASE_STATUS
    CASE_vals = list(h1b_data.CASE_STATUS.unique())
    numbers = list(range(len(CASE_vals)))
    CASE_vals_dict = dict(zip(CASE_vals, numbers))


    #Preparing WORKSITE
    state_list = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming','District of Columbia','Puerto Rico','Guam','American Samoa','U.S. Virgin Islands','Northern Mariana Islands']

    for state in state_list:
        h1b_data.WORKSITE = h1b_data.WORKSITE.apply(lambda x: state.upper() if state.upper() in x else x)    

    #Renaming WORKSITE
    WORK_vals = list(h1b_data.WORKSITE.unique())
    numbers = list(range(len(WORK_vals)))
    WORK_vals_dict = dict(zip(WORK_vals, numbers))


    #Renaming JOB_TITLE
    JOB_vals = list(h1b_data.JOB_TITLE.unique())
    numbers = list(range(len(JOB_vals)))
    JOB_vals_dict = dict(zip(JOB_vals, numbers))


    h1b_data.replace(SOC_vals_dict, inplace=True)
    h1b_data.replace(CASE_vals_dict, inplace=True)
    h1b_data.replace(WORK_vals_dict, inplace=True)
    h1b_data.replace(JOB_vals_dict, inplace=True)
    h1b_data.dropna(inplace=True);

    df = h1b_data
    df_norm = (df - df.mean()) / (df.max() - df.min())
    h1b_data['lon'] = df_norm['lon']
    h1b_data['lat'] = df_norm['lat']
    h1b_data['PREVAILING_WAGE'] = df_norm['PREVAILING_WAGE']
    h1b_data = h1b_data[h1b_data.CASE_STATUS != 1]

    h1b_data['CASE_STATUS'].replace({0:1, 2:1, 3:0}, inplace=True)
    
    return h1b_data;
