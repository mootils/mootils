import numpy as np
from scipy import spatial

from mootils.qualityindicator.quality_indicator import QualityIndicator


class InvertedGenerationalDistancePlus(QualityIndicator):
    """ Inverted generational distance plus quality indicator, defined in :
        Hisao Ishibuchi, Hiroyuki Masuda, Yusuke Nojima: A Study on Performance Evaluation Ability of a Modified
        Inverted Generational Distance Indicator. GECCO 2015: 695-702
    """
    def __init__(self, reference_front: np.array):
        super(InvertedGenerationalDistancePlus, self).__init__()
        self.reference_front = reference_front

    def compute(self, front: np.array, **kwargs) -> float:
        if self.reference_front is None:
            raise Exception('Reference front is none')

        sum = 0.0
        for i in range(len(self.reference_front)):
             sum += self.__distance_to_closest_point(self.reference_front[i], front)

        return sum/len(self.reference_front)

    def get_short_name(self) -> str:
        return 'IGD+'

    def get_name(self) -> str:
        return 'Inverted Generational Distance Plus'

    def __dominance_distance(self, point1: np.array, point2: np.array) -> float:
        return np.sqrt(sum(pow(max(point2[i]-point1[i], 0.0), 2.0) for i in range(len(point1))))

    def __distance_to_closest_point(self, point: np.array, front: np.array):
        return min(self.__dominance_distance(point, front[i]) for i in range(len(front)))
