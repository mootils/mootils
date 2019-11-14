import numpy as np
from scipy import spatial

from mootils.qualityindicator.quality_indicator import QualityIndicator


class GenerationalDistance(QualityIndicator):

    def __init__(self, reference_front: np.array):
        """
        * Van Veldhuizen, D.A., Lamont, G.B.: Multiobjective Evolutionary Algorithm Research: A History and Analysis.
          Technical Report TR-98-03, Dept. Elec. Comput. Eng., Air Force. Inst. Technol. (1998)
        """
        super(GenerationalDistance, self).__init__()
        self.reference_front = reference_front

    def compute(self, front: np.array, **kwargs) -> float:
        if self.reference_front is None:
            raise Exception('Reference front is none')

        distances = spatial.distance.cdist(front, self.reference_front)

        return np.mean(np.min(distances, axis=1))

    def get_short_name(self) -> str:
        return 'GD'

    def get_name(self) -> str:
        return 'Generational Distance'
