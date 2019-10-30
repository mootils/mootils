import unittest
import os
import numpy as np

from mootils.qualityindicator.hypervolume.fonsecahypervolume import FonsecaHyperVolume
from mootils.util.matrix_utils import read_matrix_from_file

root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path_to_pareto_front = os.path.join(root, "../resources", "paretofronts")

class HypervolumeTestCases(unittest.TestCase):

    def test_should_constructor_create_a_non_null_object(self) -> None:
        indicator = FonsecaHyperVolume(reference_point=[])
        self.assertIsNotNone(indicator)

    def test_get_name_return_the_right_value(self):
        self.assertEqual("Hypervolume proposed by Fonseca et al.", FonsecaHyperVolume([]).get_name())

    def test_get_short_name_return_the_right_value(self):
        self.assertEqual("HV", FonsecaHyperVolume([]).get_short_name())

    def test_should_hypervolume_return_5_0(self):
        reference_point = [2, 2, 2]

        front = np.array([[1.0, 0.0, 1.0], [0.0, 1.0, 0.0]])

        hv = FonsecaHyperVolume(reference_point)
        value = hv.compute(front)

        self.assertEqual(5.0, value)

    def test_should_hypervolume_return_the_correct_value_when_applied_to_the_ZDT1_reference_front(self):
        front = read_matrix_from_file(os.path.join(path_to_pareto_front, "ZDT1.pf"))

        reference_point = [1, 1]

        hv = FonsecaHyperVolume(reference_point)
        value = hv.compute(front)

        self.assertAlmostEqual(0.666, value, delta=0.001)


if __name__ == '__main__':
    unittest.main()
