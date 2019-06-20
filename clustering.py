from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from pandas import DataFrame
from rpy2.robjects import DataFrame, FloatVector, IntVector
from rpy2.robjects.packages import importr
from math import isclose
from kmodes.kmodes import KModes
import numpy as np

# TODO fix hyper-param in functions
def kmeans(data, isfast):
    # Data = {
    #     'x': [25, 34, 22, 27, 33, 33, 31, 22, 35, 34, 67, 54, 57, 43, 50, 57, 59, 52, 65, 47, 49, 48, 35, 33, 44, 45,
    #           38, 43, 51, 46],
    #     'y': [79, 51, 53, 78, 59, 74, 73, 57, 69, 75, 51, 32, 40, 47, 53, 36, 35, 58, 59, 50, 25, 20, 14, 12, 20, 5, 29,
    #           27, 8, 7]
    #     }
    # if isfast is tru fastkmeans called

    df = DataFrame(data, columns=['x', 'y'])
    if isfast:
        kmeans = KMeans(n_clusters=3).fit(df)
    else:
        kmeans = KMeans(n_clusters=3, init="random").fit(df)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    return labels;


def dbscan(data):
    # X = np.array([[1, 2], [2, 2], [2, 3],
    #               [8, 7], [8, 8], [25, 80]])
    clustering = DBSCAN(eps=3, min_samples=2).fit(data)
    return clustering.labels_


def kmode(data):
    # kmode for categorical data

    # random categorical data
    data = np.random.choice(20, (100, 10))
    km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)

    clusters = km.fit_predict(data)
    return clusters


def icc():
    # TODO fix icc
    groups = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4,
              4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]
    values = [1, 2, 0, 1, 1, 3, 3, 2, 3, 8, 1, 4, 6, 4, 3,
              3, 6, 5, 5, 6, 7, 5, 6, 2, 8, 7, 7, 9, 9, 9, 9, 8]

    r_icc = importr("ICC")
    df = DataFrame({"groups": IntVector(groups),
                    "values": FloatVector(values)})
    icc_res = r_icc.ICCbare("groups", "values", data=df)
    icc_val = icc_res[0]  # icc_val now holds the icc value

    # check whether icc value equals reference value
    print(isclose(icc_val, 0.728, abs_tol=0.001))

icc()