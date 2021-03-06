from scipy import stats as ss
import factor_analyzer as fa
import math
import numpy as np
import scipy.stats as st


def chisquare_test(number_list):
    chsq, pval = ss.chisquare(number_list)

    return chsq, pval


def t_test(number_list1, number_list2):
    t, pval = ss.ttest_ind(number_list1, number_list2)
    return t, pval


def anova(*args):
    fval, pval = ss.f_oneway(*args)
    return fval, pval


def kruskal_test(*args):
    krusk, pval = ss.kruskal(*args)
    return krusk, pval


def mannwhitney_test(number_list1, number_list2):
    manwhit, pval = ss.mannwhitneyu(number_list1, number_list2)
    return manwhit, pval


def median_test(*args):
    median, pval, m, table = ss.median_test(*args)
    return median, pval, m, table


def normal_test(number_list):
    normal, pval = ss.normaltest(number_list)
    return normal, pval


def korvit(data):
    # korvit
    # data is matrix
    # https://www.datacamp.com/community/tutorials/introduction-factor-analysis
    chi_square_value, p_value = fa.factor_analyzer.calculate_bartlett_sphericity(data)
    if math.isnan(chi_square_value):
        chi_square_value = 0
    if math.isnan(p_value):
        p_value = 0
    return chi_square_value, p_value


def kmo(data):
    kmo_all, kmo_model = fa.factor_analyzer.calculate_kmo(data)
    if kmo_all is None:
        kmo_all = 0
    if kmo_model is None:
        kmo_model = 0
    return kmo_all, kmo_model


def exploratory_factor_analyzer(data_feature):
    # https://pypi.org/project/factor-analyzer/
    factora = fa.FactorAnalyzer(rotation=None)
    factora.fit(data_feature)
    return factora.loadings_, factora.get_communalities()


def confirmatory_factor_analyzer(data_feature):
    # https://pypi.org/project/factor-analyzer/
    # data_featur is matrix that colomn are faeturename
    # model_dict = {"d": ["s","group","group"],
    #               "s": ["group"]}
    factora = fa.FactorAnalyzer(rotation=None)
    model_spec = fa.ModelSpecificationParser.parse_model_specification_from_dict(data_feature)
    cfa = fa.ConfirmatoryFactorAnalyzer(model_spec, disp=False)
    cfa.fit(data_feature.values)

    factora.fit(data_feature)
    loadings, varcovs, trans = cfa.loadings_, cfa.factor_varcovs_, cfa.transform(data_feature.values)
    return loadings, varcovs, trans


def spearman_test(p_value, alpha):
    correlation = 0
    if p_value < alpha:
        # correlated
        correlation = 1
    return correlation


def pearson_test(p_value, alpha):
    correlation = 0
    if p_value < alpha:
        # correlated
        correlation = 1
    return correlation


def kendalltau_test(p_value, alpha):
    correlation = 0
    if p_value < alpha:
        # correlated
        correlation = 1
    return correlation


def cramersv_test(coefficient, treshhold):
    association = 0
    if coefficient > treshhold:
        # associated
        association = 1
    return association


def somersd_test(coefficient, treshhold):
    association = 0
    direction = 1

    if coefficient < 0:
        direction = -1

    if math.fabs(coefficient) > treshhold:
        # associated
        association = 1

    return association, direction


def cohen_test(coefficient, treshhold):
    agreement = 0

    if coefficient >= treshhold:
        # agreement
        agreement = 1

    return agreement


def random_test(list, alpha=0.05):
    # https://medium.com/@sddkal/runs-test-implementation-in-python-6236b0a2b433
    # Get positive and negative values
    v=np.median(list)
    mask = list > v
    # get runs mask
    p = mask == True
    n = mask == False
    xor = np.logical_xor(p[:-1], p[1:])
    # A run can be identified by positive
    # to negative (or vice versa) changes
    list = sum(xor) + 1  # Get number of runs

    n_p = sum(p)  # Number of positives
    n_n = sum(n)
    # Temporary intermediate values
    tmp = 2 * n_p * n_n
    tmps = n_p + n_n
    # Expected value
    r_hat = np.float64(tmp) / tmps + 1
    # Variance
    s_r_squared = (tmp * (tmp - tmps)) / (tmps * tmps * (tmps - 1))
    # Standard deviation
    s_r = np.sqrt(s_r_squared)
    # Test score
    z = (list - r_hat) / s_r

    # Get normal table
    z_alpha = st.norm.ppf(1 - alpha)
    # Check hypothesis
    return z, z_alpha



