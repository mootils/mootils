import logging

import numpy as np

LOGGER = logging.getLogger('mootils')


def read_matrix_from_file(file_name: str) -> np.array:
    """ Reads a two-dimension float matrix from a file. Typically, this matrix will represented a front of objective
    vectors. The expected content is a file containing M lines where each line contains a list of N double values
    separated by spaces and/or tabs. M represents the number of vectors and N is the dimension of each vector
    (i.e., the number of objectives)

     Parameters
    ----------
    file_name : str
            File path of the file containing the data.

    Returns
    -------
    np.array
            The value of the quality indicator
    """

    matrix = np.loadtxt(file_name)

    return matrix
