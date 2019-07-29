import statistics as st
from scipy import stats as ss
import numpy as np
import pandas as pd
import sklearn
from psy import sem
import math


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
    index=[]
    for i in range(15177):
        index.append(i)
    table = pd.DataFrame.from_records({'numbers1': x, 'numbers2': y} )
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
    sklearn.metrics.cohen_kappa_score(input1, input2, labels=None, weights=None)


def somersd(score, target):
    score, target = (list(t) for t in zip(*sorted(zip(score, target))))
    ttl_num = len(score)
    bin = 20;
    n = ttl_num / 20;
    sum_target = sum(target);
    sum_notarget = ttl_num - sum_target;
    pct_target = [];
    pct_notarget = [];
    pct_target.append(0.0);
    pct_notarget.append(0.0);
    for i in range(1, bin):
        if (i != bin):
            pct_target.append((sum(target[0:(i * n - 1)]) + 0.0) / sum_target);
            pct_notarget.append((i * n - sum(target[0:(i * n - 1)]) + 0.0) / sum_notarget)

    pct_target.append(1.0);
    pct_notarget.append(1.0);
    sd = []
    for i in range(1, bin + 1):
        sd.append((pct_target[i] + pct_target[i - 1]) * (pct_notarget[i] - pct_notarget[i - 1]));
    somersd = 1 - sum(sd);
    return (somersd);


def anova_eta_omg(data):
    # https://www.marsja.se/four-ways-to-conduct-one-way-anovas-using-python/

    # data shape : 3*30
    # id , weight , group is col name :weight is float , group is 3 variety of string

    N = len(data.values)  # conditions times participants
    n = data.groupby('group').size()[0]
    k = len(pd.unique(data.group))

    DFbetween = k - 1
    DFwithin = N - k
    DFtotal = N - 1

    SSbetween = (sum(data.groupby('group').sum()['weight'] ** 2) / n) \
                - (data['weight'].sum() ** 2) / N
    sum_y_squared = sum([value ** 2 for value in data['weight'].values])
    SSwithin = sum_y_squared - sum(data.groupby('group').sum()['weight'] ** 2) / n
    SStotal = sum_y_squared - (data['weight'].sum() ** 2) / N
    MSwithin = SSwithin / DFwithin

    eta_sqrd = SSbetween / SStotal
    om_sqrd = (SSbetween - (DFbetween * MSwithin)) / (SStotal + MSwithin)
    return eta_sqrd, om_sqrd


def structural_equation_modeling(data, y, x, lam_x, lam_y, beta, gamma):
    # https: // github.com / inuyasha2012 / pypsy / blob / master / demo / demo_sem.py
    lam_x, lam_y, phi_x, beta, gamma, var_e, var_e_x, var_e_y = sem(data, y, x, lam_x, lam_y, beta, gamma)
    return lam_x, lam_y, phi_x, beta, gamma, var_e, var_e_x, var_e_y


def payaii(itemscores):
    # CronbachAlpha
    # https://fa.wikipedia.org/wiki/%D8%A2%D8%B2%D9%85%D9%88%D9%86_%DA%A9%D8%B1%D9%88%D9%86%D8%A8%D8%A7%D8%AE_%D8%A2%D9%84%D9%81%D8%A7
    # itemscores = [[4, 14, 3, 3, 23, 4, 52, 3, 33, 3], [5, 14, 4, 3, 24, 5, 55, 4, 15, 3]]

    itemvars = [st.variance(item) for item in itemscores]
    tscores = [0] * len(itemscores[0])
    for item in itemscores:
        for i in range(len(item)):
            tscores[i] += item[i]
    nitems = len(itemscores)

    Calpha = nitems / (nitems - 1.) * (1 - sum(itemvars) / st.variance(tscores))

    return Calpha


def point_biserial(list_number1, list_number2):
    rval, p_val = ss.pointbiserialr(list_number1, list_number2)
    return rval, p_val


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
            row.append(point_biserial(item1, item2))
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
