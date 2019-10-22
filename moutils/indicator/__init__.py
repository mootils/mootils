from abc import ABC, abstractmethod

import numpy as np


class QualityIndicator(ABC):

    @abstractmethod
    def compute(self, solutions: np.array, **kwargs):
        """
        :param solutions: [m, n] bi-dimensional numpy array, being ``m`` the number of solutions and ``n`` the dimension
        of each solution.
        :return: The result value of the quality indicator.
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_short_name(self) -> str:
        pass
