from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from pandas import DataFrame
import pandas as pd
from kmodes.kmodes import KModes
import numpy as np
import pyreadstat
import imputation as imp


def kmeans(data, ncluster):
    # df, meta = pyreadstat.read_sav("/Users/alireza/project/DMTM/flask/er0827t.sav")
    df = data
    k = KMeans(n_clusters=ncluster).fit(df)
    return k.labels_.tolist(), k.cluster_centers_.tolist()


def dbscan(data, eps, min_samples):
    # df, meta = pyreadstat.read_sav("/Users/alireza/project/DMTM/flask/er0827t.sav")
    df = data
    labels = DBSCAN(eps=eps, min_samples=min_samples).fit_predict(df)
    return labels


def kmode(data, ncluster, n_init, verbose):
    # kmode for categorical data

    # random categorical data
    data = np.random.choice(20, (100, 10))
    km = KModes(n_clusters=ncluster, init='Huang', n_init=n_init, verbose=verbose)

    clusters = km.fit_predict(data)
    return clusters

# csv = pd.read_csv("/Users/alireza/project/DMTM/flask/files/sample3.csv")
# label=dbscan(csv,3,2)
# label=dbscan(csv,3,2)
