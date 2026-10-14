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
def fit(xtr, ytr):
    n_classes = np.unique(ytr).size
    n_features = xtr.shape[1]
    centroids = np.zeros(shape=(n_classes, n_features))
    for k in range(n_classes):
        centroids[k,:] = np.mean(xtr[ytr == k , :] , axis=0)
    return centroids


centroids = fit(xtr, ytr)
plot_ten_digits(centroids)
plt.show()
