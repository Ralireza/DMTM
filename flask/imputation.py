import random
import descriptive_feature as df
import math
import sys
from impyute.imputation.cs import fast_knn
import numpy as np
import pandas as pd
from sklearn import linear_model

sys.setrecursionlimit(100000)  # Increase the recursion limit of the OS


def imputation(number_list, mode, k=3):
    if mode is 'knn':
        imputed_training = fast_knn(number_list, k)
        return imputed_training
    elif mode is 'random':
        cleanedList = []
        for i in number_list:
            if not math.isnan(i):
                cleanedList.append(i)
        for index, value in enumerate(number_list):
            if math.isnan(value):
                number_list[index] = random.choice(cleanedList)
        return number_list
    elif mode is 'regression':
        number_list = reg_impute(number_list)
        return number_list
    elif mode is 'frequency':
        cleanedList = []
        for i in number_list:
            if not math.isnan(i):
                cleanedList.append(i)
        for index, value in enumerate(number_list):
            if math.isnan(value):
                number_list[index] = df.mode(cleanedList)
        return number_list
    elif mode is 'mean':
        cleanedList = []
        for i in number_list:
            if not math.isnan(i):
                cleanedList.append(i)
        for index, value in enumerate(number_list):
            if math.isnan(value):
                number_list[index] = df.mean(cleanedList)
        return number_list


def random_imputation(dd, feature):
    number_missing = dd[feature].isnull().sum()
    observed_values = dd.loc[dd[feature].notnull(), feature]
    dd.loc[dd[feature].isnull(), feature + '_imp'] = np.random.choice(observed_values, number_missing, replace=True)
    return dd


def reg_impute(csv):
    missing_columns = csv.columns.values
    final_list = {}
    for feature in missing_columns:
        csv[feature + '_imp'] = csv[feature]
        csv = random_imputation(csv, feature)
    deter_data = pd.DataFrame(columns=["Det" + name for name in missing_columns])

    for feature in missing_columns:
        deter_data["Det" + feature] = csv[feature + "_imp"]
        parameters = list(set(csv.columns) - set(missing_columns) - {feature + '_imp'})

        # Create a Linear Regression model to estimate the missing data
        model = linear_model.LinearRegression()
        model.fit(X=csv[parameters], y=csv[feature + '_imp'])

        # observe that I preserve the index of the missing data from the original dataframe
        deter_data.loc[csv[feature].isnull(), "Det" + feature] = model.predict(csv[parameters])[csv[feature].isnull()]
    for feature in missing_columns:
        final_list[feature] = (list(csv[feature + "_imp"]))
    return final_list


