import unittest

import numpy as np

from mootils.qualityindicator.generational_distance import GenerationalDistance
from mootils.qualityindicator.inverted_generational_distance_plus import InvertedGenerationalDistancePlus


class InvertedGenerationalDistancePlusTestCases(unittest.TestCase):

    def test_should_constructor_create_a_non_null_object(self) -> None:
        indicator = InvertedGenerationalDistancePlus([])
        self.assertIsNotNone(indicator)

    def test_get_name_return_the_right_value(self):
        self.assertEqual("Inverted Generational Distance Plus", InvertedGenerationalDistancePlus([]).get_name())

    def test_get_short_name_return_the_right_value(self):
        self.assertEqual("IGD+", InvertedGenerationalDistancePlus([]).get_short_name())

    def test_case1(self):
        """
        Case 1. Reference front: [[1.0, 1.0]], front: [[1.0, 1.0]]
        Expected result: the distance to the nearest point of the reference front is 0.0
        :return:
        """
        indicator = InvertedGenerationalDistancePlus(np.array([[1.0, 1.0]]))
        front = np.array([[1.0, 1.0]])

        result = indicator.compute(front)

        self.assertEqual(0.0, result)

    def test_case2(self):
        """
        Case 2. Reference front: [[0.1, 0.7], [0.2, 0.3], [0.6, 0.2]], front: [[0.2, 0.5], [0.3, 0.4], [0.4, 0.3]]
        Expected result:  0.11380711874576983
        :return:
        """
        indicator = InvertedGenerationalDistancePlus(np.array([[0.1, 0.7], [0.2, 0.3], [0.6, 0.2]]))
        front = np.array([[0.2, 0.5], [0.3, 0.4], [0.4, 0.3]])

        result = indicator.compute(front)

        self.assertEqual(0.11380711874576983, result)

    def test_case3(self):
        """
        Case 3. Reference front: [[0.1, 0.7], [0.2, 0.3], [0.6, 0.2]], front: [[0.3, 0.7], [0.5, 0.6], [0.7, 0.4]]
        Expected result:  0.278639120103915.
        :return:
        """
        indicator = InvertedGenerationalDistancePlus(np.array([[0.1, 0.7], [0.2, 0.3], [0.6, 0.2]]))
        front = np.array([[0.3, 0.7], [0.5, 0.6], [0.7, 0.4]])

        result = indicator.compute(front)

        self.assertAlmostEqual(0.278639120103915, result)

