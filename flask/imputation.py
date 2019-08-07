import random
import descriptive_feature as df
from fancyimpute import KNN


def imputation(number_list, missing_index, mode,k=3):
    if mode is 'knn':
        X_filled_knn = KNN(k=k).fit_transform(number_list)
        return X_filled_knn
    elif mode is 'random':
        number_list[missing_index] = random.choice(number_list)
        return number_list
    elif mode is 'regression':
        # TODO icant find any function
        return number_list
    elif mode is 'frequency':
        mode = df.mode(number_list)
        number_list[missing_index] = mode
        return number_list
    elif mode is 'mean':
        mean = df.mean(number_list)
        number_list[missing_index] = mean
        return number_list
