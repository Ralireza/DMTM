from scipy import stats as ss
import factor_analyzer as fa


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


def sphericity(data):
    # korvit
    # data is matrix
    # https://www.datacamp.com/community/tutorials/introduction-factor-analysis
    chi_square_value, p_value = fa.calculate_bartlett_sphericity(data)
    return chi_square_value, p_value


def kmo(data):
    kmo_all, kmo_model = fa.calculate_kmo(data)
    return kmo_all, kmo_model


def exploratory_factor_analyzer(data_feature):
    # https://pypi.org/project/factor-analyzer/
    factora = fa.FactorAnalyzer(rotation=None)
    factora.fit(data_feature)
    return factora.loadings_, factora.get_communalities()


def confirmatory_factor_analyzer(data_feature, model_dict):
    # https://pypi.org/project/factor-analyzer/
    # data_featur is matrix that colomn are faeturename
    # model_dict = {"F1": ["V1", "V2", "V3", "V4"],
    #                  "F2": ["V5", "V6", "V7", "V8"]}
    factora = fa.FactorAnalyzer(rotation=None)
    model_spec = fa.ModelSpecificationParser.parse_model_specification_from_dict(data_feature, model_dict)
    cfa = fa.ConfirmatoryFactorAnalyzer(model_spec, disp=False)
    cfa.fit(data_feature.values)

    factora.fit(data_feature)
    return cfa.loadings_, cfa.factor_varcovs_, cfa.transform(data_feature.values)
