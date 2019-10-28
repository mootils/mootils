import numpy as np

from mootils.indicator import QualityIndicator


class EpsilonIndicator(QualityIndicator):

    def __init__(self, reference_front: np.array):
        super(EpsilonIndicator).__init__()
        self.reference_front = reference_front

    def compute(self, solutions: np.array, **kwargs) -> float:
        return max([min(
            [max([s2[k] - s1[k] for k in range(len(s2))]) for s2 in solutions]) for s1 in self.reference_front])

    def get_short_name(self) -> str:
        return 'EP'

    def get_name(self) -> str:
        return "Additive Epsilon"
