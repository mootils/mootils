from pathlib import Path

import numpy as np
import logging

LOGGER = logging.getLogger('mootils')


def read_solutions_from_file(file_name: str) -> np.array:
    """ Reads a front of solutions from a file. The expected content is a file containing M lines where each line
    contains a list of N double values separated by spaces and/or tabs. M represents the number of solutions, and N is
    the dimension of each solution (i.e., the number of objectives)

     Parameters
    ----------
    file_name : str
            File path of the file containing the data.

    Returns
    -------
    np.array
            The value of the quality indicator
    """
    front = np.loadtxt(file_name)

    return front
