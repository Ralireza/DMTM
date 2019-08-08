import random
import descriptive_feature as df
from fancyimpute import KNN
import math


def imputation(number_list, mode, k=3):
    if mode is 'knn':
        X_filled_knn = KNN(k=k).fit_transform(number_list)
        return X_filled_knn
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
        # TODO icant find any function
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
