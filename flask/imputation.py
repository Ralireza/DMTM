import random
import descriptive_feature as df
import math
import sys
from impyute.imputation.cs import fast_knn
import numpy as np
import pandas as pd
from sklearn import linear_model
from scipy import stats as ss
from operator import itemgetter

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

    elif mode is 'corrected':
        number_list = correct_impute(number_list)
        return number_list

    elif mode is 'fard':
        number_list = fard_impute(number_list)
        return number_list

    elif mode is 'porsesh':
        number_list = porsesh_impute(number_list)
        return number_list

    elif mode is 'hambaste':
        number_list = hambaste_impute(number_list)
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


def correct_impute(number_list):
    empty_row = set()
    for index, row in number_list.iterrows():
        for one in row:
            if math.isnan(one):
                empty_row.add(index)

    for row in empty_row:
        q_means = []
        user_means = []

        for col in number_list:
            q_means.append(number_list[col].mean())
        mean_user = number_list.iloc[row].mean()

        for q in q_means:
            user_means.append(q - mean_user)

        final_mean = sum(user_means) / len(user_means)

        for index, value in enumerate(number_list.iloc[row]):
            if math.isnan(value):
                number_list.iloc[row, index] = q_means[index] + final_mean
        dict = number_list.to_dict('dict')
    return dict


def fard_impute(number_list):
    empty_row = set()
    for index, row in number_list.iterrows():
        for one in row:
            if math.isnan(one):
                empty_row.add(index)
    for row in empty_row:
        mean_user = number_list.iloc[row].mean()
        for index, value in enumerate(number_list.iloc[row]):
            if math.isnan(value):
                number_list.iloc[row, index] = mean_user
        dict = number_list.to_dict('dict')
    return dict


def porsesh_impute(number_list):
    empty_col = set()
    for col in number_list:
        for one in number_list[col]:
            if type(one) is not str:
                if math.isnan(one):
                    empty_col.add(col)
    for col in empty_col:
        mean_user = number_list[col].mean()
        for index, value in enumerate(number_list[col]):
            if math.isnan(value):
                number_list[col][index] = mean_user
        dict = number_list.to_dict('dict')
    return dict


def hambaste_impute(number_list):
    # find empty rows
    empty_row = []
    for index, row in number_list.iterrows():
        for one in row:
            if math.isnan(one):
                empty_row.append(index)

    # delete empty rows
    deleted_empty_rows=number_list
    for row in empty_row:
        deleted_empty_rows = deleted_empty_rows.drop(row)

    # find empty col
    empty_position = []
    for indx, col in enumerate(number_list):
        for ind,one in enumerate(number_list[col]):
            if type(one) is not str:
                if math.isnan(one):
                    empty_position.append([col,ind])

    # find most correlated col TODO just for one empty
    col_to_compare_with = [x for x in list(number_list.columns.values) if x not in empty_position[0]]
    result_corr = []
    for non_value in (empty_position):
        empty_col=non_value[0]
        empty_row=non_value[1]
        for cmp in col_to_compare_with:
            correlation, p = ss.pearsonr(deleted_empty_rows[col], deleted_empty_rows[cmp])
            result_corr.append([col, cmp, math.fabs(correlation)])

        indx, value = max(enumerate(map(itemgetter(-1), result_corr)), key=itemgetter(1))
        most_corr_col = result_corr[indx][1]
        neighbour_in_corr_col = number_list[most_corr_col][empty_row]

        if list(number_list[most_corr_col]).count(neighbour_in_corr_col) > 1:
            nearest_neighbour = neighbour_in_corr_col
        else:
            all_sub = []
            for indx, val in enumerate(number_list[most_corr_col]):
                if indx != empty_row:
                    all_sub.append([val,abs(val - neighbour_in_corr_col)])
            innd,nearest_neighbour = min(enumerate(map(itemgetter(-1), all_sub)), key=itemgetter(1))
            nearest_neighbour=all_sub[innd][0]
        if list(number_list[most_corr_col]).count(nearest_neighbour) > 1:
            all_row_corr = []
            # impute by mean of all of theme
            for indx, val in enumerate(number_list[most_corr_col]):
                if val == nearest_neighbour and indx != empty_row:
                    all_row_corr.append(indx)
            sum = 0
            for i in all_row_corr:
                sum = sum + number_list[col][i]

            mean = sum / len(all_row_corr)
            number_list.loc[empty_row, col] = mean

        else:
            # impute by nearest value
            for indx, val in enumerate(number_list[most_corr_col]):
                if val == nearest_neighbour:
                    imputation = indx
            number_list.loc[empty_row, empty_col] = number_list.loc[imputation, empty_col ]

        dict = number_list.to_dict('dict')

    return dict




# csv = pd.read_csv("/Users/alireza/project/DMTM/flask/files/sample6.csv")
# a = hambaste_impute(csv)
# print(a)
