import statistics as st
from scipy import stats as ss
import numpy as np
import pandas as pd


def min_num(number_list):
    return min(number_list)


def max_num(number_list):
    return max(number_list)


def range_domain(number_list):
    return max(number_list) - min(number_list)


def mean(number_list):
    return st.mean(number_list)


def trimmed_mean(number_list, limitation):
    # limitation is float number like 0.3 and delete 0.3 of outlier data
    return ss.trim_mean(number_list, limitation)


def mode(number_list):
    return st.mode(number_list)


def median(number_list):
    return st.median(number_list)


def wighted_median(number_list, w_list):
    df = pd.DataFrame({'numbers': number_list, 'weights': w_list})
    df.sort_values('numbers', inplace=True)
    cumsum = df.weights.cumsum()
    cutoff = df.weights.sum() / 2.0
    median = df.numbers[cumsum >= cutoff].iloc[0]
    return median


def variance(number_list):
    return st.variance(number_list)


def deviation(number_list):
    return st.stdev(number_list)


def quantile(number_list, q):
    # q between 0 , 1
    return np.quantile(number_list, q)


def population_skewness(number_list):
    # choolegi
    return ss.skew(number_list)


def kurtosis(number_list):
    # keshidegi
    return ss.kurtosis(number_list)
