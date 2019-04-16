import statistics as st
from scipy import stats as ss
import numpy as np
import pandas as pd
import sklearn


def pearson_correlation(list_number1, list_number2):
    return ss.pearsonr(list_number1, list_number2)


def spearman_correlation(list_number1, list_number2):
    return ss.spearmanr(list_number1, list_number2)


def kendalltau_correlation(list_number1, list_number2):
    tau, p_value = ss.kendalltau(list_number1, list_number2)
    return tau, p_value


def cramers_v(x, y):
    confusion_matrix = pd.crosstab(x, y)
    chi2 = ss.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))


def tavafoghi(input1, input2):
    # TODO idont know what
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


def anova_table(aov):
    # https: // pythonfordatascience.org / anova - python /
    aov['mean_sq'] = aov[:]['sum_sq'] / aov[:]['df']

    aov['eta_sq'] = aov[:-1]['sum_sq'] / sum(aov['sum_sq'])

    aov['omega_sq'] = (aov[:-1]['sum_sq'] - (aov[:-1]['df'] * aov['mean_sq'][-1])) / (
                sum(aov['sum_sq']) + aov['mean_sq'][-1])

    cols = ['sum_sq', 'df', 'mean_sq', 'F', 'PR(>F)', 'eta_sq', 'omega_sq']
    aov = aov[cols]
    return aov


