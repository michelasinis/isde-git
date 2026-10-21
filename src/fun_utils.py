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
    Split the data X,y into two random subsets

    """
    pass



    Xtr = x[tr_idx, :]
    ytr = y[tr_idx]

    Xts = x[ts_idx, :]
    yts = y[ts_idx]

    return Xtr, ytr, Xts, yts
#try to add a comment
