from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from pandas import DataFrame
# from rpy2.robjects import DataFrame, FloatVector, IntVector
# from rpy2.robjects.packages import importr
from math import isclose
from kmodes.kmodes import KModes
import numpy as np


def kmeans(data, ncluster, isfast):
    # if isfast is tru fastkmeans called

    df = DataFrame(data)
    if isfast:
        kmeans = KMeans(n_clusters=ncluster).fit(df)
    else:
        kmeans = KMeans(n_clusters=ncluster, init="random").fit(df)
    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_
    return labels


def dbscan(data,eps,min_samples):
    clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(data)
    return clustering.labels_


def kmode(data, ncluster, n_init, verbose):
    # kmode for categorical data

    # random categorical data
    data = np.random.choice(20, (100, 10))
    km = KModes(n_clusters=ncluster, init='Huang', n_init=n_init, verbose=verbose)

    clusters = km.fit_predict(data)
    return clusters


# def icc():
#     # TODO fix icc
#     groups = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4,
#               4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8]
#     values = [1, 2, 0, 1, 1, 3, 3, 2, 3, 8, 1, 4, 6, 4, 3,
#               3, 6, 5, 5, 6, 7, 5, 6, 2, 8, 7, 7, 9, 9, 9, 9, 8]
#
#     r_icc = importr("ICC")
#     df = DataFrame({"groups": IntVector(groups),
#                     "values": FloatVector(values)})
#     icc_res = r_icc.ICCbare("groups", "values", data=df)
#     icc_val = icc_res[0]  # icc_val now holds the icc value
#
#     # check whether icc value equals reference value
#     print(isclose(icc_val, 0.728, abs_tol=0.001))
#
#

