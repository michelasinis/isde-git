from pandas import read_csv
import numpy as np


def load_data(filename):
    """
    Load data from a csv file

    Parameters
    ----------
    filename : string
        Filename to be loaded.

    Returns
    -------
    X : ndarray
        the data matrix.

    y : ndarray
        the labels of each sample.
    """
    data = read_csv(filename)
    z = np.array(data)
    y = z[:, 0]
    X = z[:, 1:]
    return X, y


def split_data(x, y, tr_fraction=0.5):
    """
    Split the data x, y into two random subsets

    """
    pass



# predict
from sklearn.metrics import pairwise_distances

def predict(xts, centroids):
    dist = pairwise_distances(xts, centroids)
    ypred = np.argmin(dist, axis=1)
    return ypred

ypred = predict(xts, centroids)
print(ypred)
print(yts)

print("error: ", np.mean(ypred != yts))


