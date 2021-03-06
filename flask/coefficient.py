import statistics as st
from scipy import stats as ss
import numpy as np
import pandas as pd
from sklearn import metrics
import math
from semopy import Model
from semopy import Optimizer
from semopy.inspector import inspect


def pearson_correlation(list_number1, list_number2):
    correlation, p_value = ss.pearsonr(list_number1, list_number2)
    return correlation, p_value


def spearman_correlation(list_number1, list_number2):
    correlation, p_value = ss.spearmanr(list_number1, list_number2)
    return correlation, p_value


def kendalltau_correlation(list_number1, list_number2):
    correlation, p_value = ss.kendalltau(list_number1, list_number2)
    return correlation, p_value


def cramers_v(x, y):
    index = []
    for i in range(15177):
        index.append(i)
    table = pd.DataFrame.from_records({'numbers1': x, 'numbers2': y})
    confusion_matrix = pd.crosstab(table.numbers1, table.numbers2)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))


def tavafoghi(input1, input2):
    return metrics.cohen_kappa_score(input1, input2, labels=None, weights=None)


def somersd(list_number1, list_number2):
    # https://en.wikipedia.org/wiki/Somers'_D
    corr1, p1 = kendalltau_correlation(list_number1, list_number2)
    corr2, p2 = kendalltau_correlation(list_number1, list_number1)
    somerd = corr1 / corr2
    return somerd


def anova_eta_omg(numlist1, numlist2):
    # https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/
    data = pd.DataFrame.from_records({'weight': numlist1, 'group': numlist2})

    N = len(data.values)  # conditions times participants
    n = data.groupby('group').size()[0]
    k = len(pd.unique(data.group))

    DFbetween = k - 1
    DFwithin = N - k

    SSbetween = (sum(data.groupby('group').sum()['weight'] ** 2) / n) \
                - (data['weight'].sum() ** 2) / N
    sum_y_squared = sum([value ** 2 for value in data['weight'].values])
    SSwithin = sum_y_squared - sum(data.groupby('group').sum()['weight'] ** 2) / n
    SStotal = sum_y_squared - (data['weight'].sum() ** 2) / N
    MSwithin = SSwithin / DFwithin

    eta_sqrd = SSbetween / SStotal
    om_sqrd = (SSbetween - (DFbetween * MSwithin)) / (SStotal + MSwithin)
    return eta_sqrd, om_sqrd


def structural_equation_modeling(data, mod):
    model = Model(mod)
    model.load_dataset(data)
    opt = Optimizer(model)
    objective_function_value = opt.optimize()
    result = inspect(opt, mode='mx')
    beta = result[0][1].to_dict('dict')
    lam = result[1][1].to_dict('dict')
    psi = result[2][1].to_dict('dict')
    theta = result[3][1].to_dict('dict')
    sigma = result[4][1].to_dict('dict')
    cov = result[5][1].to_dict('dict')

    return beta, lam, psi, theta, sigma, cov


def payaii(list_number1, list_number2):
    # CronbachAlpha
    # https://fa.wikipedia.org/wiki/%D8%A2%D8%B2%D9%85%D9%88%D9%86_%DA%A9%D8%B1%D9%88%D9%86%D8%A8%D8%A7%D8%AE_%D8%A2%D9%84%D9%81%D8%A7
    # itemscores = [[4, 14, 3, 3, 23, 4, 52, 3, 33, 3], [5, 14, 4, 3, 24, 5, 55, 4, 15, 3]]
    itemscores = [list_number1, list_number2]
    itemvars = [st.variance(item) for item in itemscores]
    tscores = [0] * len(itemscores[0])
    for item in itemscores:
        for i in range(len(item)):
            tscores[i] += item[i]
    nitems = len(itemscores)

    Calpha = nitems / (nitems - 1.) * (1 - sum(itemvars) / st.variance(tscores))

    return Calpha


def point_biserial(list_number1, list_number2):
    rval, pval = ss.pointbiserialr(list_number1, list_number2)
    return rval, pval


def biserial(list_number1, list_number2, p1, p2, y):
    # http://core.ecu.edu/psyc/wuenschk/docs30/Biserial.pdf
    # biserial = rpb*sqrt(p1 * p2)/y
    rpb, _ = point_biserial(list_number1, list_number2)
    biserial = (rpb * math.sqrt(p1 * p2)) / y
    return biserial


def get_matrix_point_biserial(*args):
    final_matrix = []
    for item1 in args:
        row = []
        for item2 in args:
            rval, pval = point_biserial(item1, item2)
            row.append(rval)
        final_matrix.append(row)
    return final_matrix


def get_matrix_biserial(p1, p2, y, *args):
    final_matrix = []
    for item1 in args:
        row = []
        for item2 in args:
            row.append(biserial(item1, item2, p1, p2, y))
        final_matrix.append(row)
    return final_matrix


def get_nomre_kol_sum(matrix, weights=None):
    final_list = []
    for i in range(len(matrix.index)):
        x = (list(matrix.iloc[i, :]))
        if weights is not None:
            w = (list(weights.iloc[i, :]))
            my_sum = sum(a * b for (a, b) in zip(x, w))
        else:
            my_sum = sum(x)
        final_list.append(my_sum)

    return final_list


def get_nomre_kol_mean(matrix, weights=None):
    final_list = []
    for i in range(len(matrix.index)):
        x = (list(matrix.iloc[i, :]))
        if weights is not None:
            w = (list(weights.iloc[i, :]))
            avg = np.average(x, weights=w)
        else:
            avg = sum(x) / len(x)
        final_list.append(avg)

    return final_list

#
#
