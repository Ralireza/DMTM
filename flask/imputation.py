import random
import descriptive_feature as df
from fancyimpute import KNN
import math
import sys
from impyute.imputation.cs import fast_knn
sys.setrecursionlimit(100000) #Increase the recursion limit of the OS


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

# imputed_training = fast_knn([1,2,3,0,5], k=2)
# print(imputed_training)