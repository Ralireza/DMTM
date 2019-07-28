import statistics as st
from scipy import stats as ss
import numpy as np


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
    return st.mmedian(number_list)


def wighted_median(number_list, w_list):
    weighted.median(number_list, w_list)


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
