from sklearn.ensemble import IsolationForest
import numpy as np
import imputation as imp
import pandas as pd
import pyreadstat
from sklearn.model_selection import train_test_split


def iso_farest(test_data, max_samples):
    df, meta = pyreadstat.read_sav("/Users/alireza/project/DMTM/flask/er0827t.sav")
    for column in df:
        if df[column].isnull().values.all():
            df.drop(columns=column, axis=1, inplace=True)
        else:
            labels = imp.imputation(df[column], "mean")
            df[column] = pd.DataFrame(labels)
    rng = np.random.RandomState(42)

    # outlier_df = []
    # for column in df:
    #     if df[column].isnull().values.all():
    #         df.drop(columns=column, axis=1, inplace=True)
    #     else:
    #         labels = imp.imputation(df[column], "mean")
    #         df[column] = pd.DataFrame(labels)
    #         mean = df[column].mean()
    #         std = df[column].std()
    #         tmp = rng.uniform(low=mean + 5 * std, high=10 * std, size=(100, 1))
    #         outlier_col = []
    #         for data in tmp:
    #             outlier_col.append(data[0])
    #         outlier_df.append(outlier_col)
    # outlier_df = pd.DataFrame(outlier_df).transpose()

    # df_all=pd.DataFrame( np.concatenate( (df.values, outlier_df.values), axis=0 ) )
    # df_all.columns=df.columns
    train, test = train_test_split(df, test_size=0.2)

    # train=df[:9999]
    # test=df[10000:]
    # anomaly = outlier_df

    # training the model
    clf = IsolationForest(max_samples=max_samples, random_state=rng)
    clf.fit(train)
    y_pred_test = clf.predict(test_data)
    # y_pred_outliers = clf.predict(anomaly)

    # new, 'normal' observations ----
    # normal_accuracy = (list(y_pred_test).count(1) / y_pred_test.shape[0])
    # outliers ----
    # outlier_accuracy = (list(y_pred_outliers).count(-1) / y_pred_outliers.shape[0])

    return y_pred_test


# csv = pd.read_csv("/Users/alireza/project/DMTM/flask/files/sample3.csv")
# labels = iso_farest(csv, 3)
# print(labels)
