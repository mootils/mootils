import logging

import numpy as np

LOGGER = logging.getLogger('mootils')


def normalize(vector: np.array, min_values: np.array = None, max_values:np.array = None) -> np.array:
    """ Normalize a vector of float values. If the minimum/maximum values are not provided, they are assumed to be
    zeroes/ones

     Parameters
    ----------
    vector : np.array
            Vector to normalize
    min_values: np.array
            Vector with minimum values
    max_values: np.array
            Vector with maximum values

    Returns
    -------
    np.array
            The normalized vector
    """

    # Initialize to default values in case the minimum and/or maximum vector values are not provided
    if min_values is None:
        min_values = np.zeros(len(vector))
    if max_values is None:
        max_values = np.ones(len(vector))

    # calculate the denominator
    denominator = max_values - min_values

    # we cannot divide by zero
    #if denominator == 0:
    #    raise Exception("Error normalizing vector: the maximum and minimum values are equal")

    return (vector - min_values) / denominator
