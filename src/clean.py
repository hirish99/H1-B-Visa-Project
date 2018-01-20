def returnClean():
    import pandas as pd
    h1b_data = pd.read_csv("../h1b_concat.csv")
    #TEMP: SHORTENED DATA:
    h1b_data = h1b_data.head(700)
    h1b_data.replace({'N':0, 'Y':1}, axis=1, inplace=True)
    h1b_data.drop(['Unnamed: 0','lon', 'lat'], axis=1, inplace=True)

    #Renaming SOC_NAME
    SOC_vals = list(h1b_data.SOC_NAME.unique())
    numbers = list(range(len(SOC_vals)))
    SOC_vals_dict = dict(zip(SOC_vals, numbers))


    #Renaming CASE_STATUS
    CASE_vals = list(h1b_data.CASE_STATUS.unique())
    numbers = list(range(len(CASE_vals)))
    CASE_vals_dict = dict(zip(CASE_vals, numbers))


    #Renaming EMPLOYER_NAME
    EMPL_vals = list(h1b_data.EMPLOYER_NAME.unique())
    numbers = list(range(len(EMPL_vals)))
    EMPL_vals_dict = dict(zip(EMPL_vals, numbers))


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
    h1b_data.replace(EMPL_vals_dict, inplace=True)
    h1b_data.replace(WORK_vals_dict, inplace=True)
    h1b_data.replace(JOB_vals_dict, inplace=True)

    return h1b_data;
