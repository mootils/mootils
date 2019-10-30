from abc import ABC, abstractmethod

import numpy as np


class QualityIndicator(ABC):

    @abstractmethod
    def compute(self, front: np.array, **kwargs) -> float:
        """
        Parameters
        ----------
        front : numpy.array
            [M, N] bi-dimensional float numpy array, being m the number of vectors and n the dimension of each of them.
            In the general case, a front represents a Pareto front approximation, so m would be the number of objective
            vectors and n the number of objectives.

        Returns
        -------
        float
            The value of the quality indicator
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_short_name(self) -> str:
        pass
