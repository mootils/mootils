import numpy as np
from scipy import spatial

from mootils.qualityindicator import QualityIndicator


class InvertedGenerationalDistance(QualityIndicator):

    def __init__(self, reference_front: np.array):
        super(InvertedGenerationalDistance, self).__init__()
        self.reference_front = reference_front

    def compute(self, solutions: np.array, **kwargs) -> np.ndarray:
        if self.reference_front is None:
            raise Exception('Reference front is none')

        distances = spatial.distance.cdist(self.reference_front, solutions)

        return np.mean(np.min(distances, axis=1))

    def get_short_name(self) -> str:
        return 'IGD'

    def get_name(self) -> str:
        return 'Inverted Generational Distance'
