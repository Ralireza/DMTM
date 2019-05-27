from sklearn.ensemble import IsolationForest
import numpy as np


def iso_farest(train_data, test_data, max_samples):
    # https://towardsdatascience.com/outlier-detection-with-isolation-forest-3d190448d45e
    clf = IsolationForest(max_samples=max_samples)
    clf.fit(train_data)

    # predictions
    pred = clf.predict(test_data)
