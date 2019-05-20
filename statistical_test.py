import statistics as st
from scipy import stats as ss
import numpy as np
import pandas as pd
import sklearn


def chisquare_test(number_list):
    return ss.chisquare(number_list)


def t_test(number_list1, number_list2):
    return ss.ttest_ind(number_list1, number_list2)


def anova(*args):
    # return f, p
    return ss.f_oneway(*args)


def kruskal_test(*args):
    return ss.kruskal(*args)


def mannwhitney_test(number_list1, number_list2):
    return ss.mannwhitneyu(number_list1, number_list2)


def median_test(*args):
    return ss.median_test(*args)


def normal_test(number_list):
    return ss.normaltest(number_list)
