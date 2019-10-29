import unittest

import numpy as np

from mootils.qualityindicator.generational_distance import GenerationalDistance


class GenerationalDistanceTestCases(unittest.TestCase):

    def test_should_constructor_create_a_non_null_object(self) -> None:
        indicator = GenerationalDistance([])
        self.assertIsNotNone(indicator)

    def test_get_name_return_the_right_value(self):
        self.assertEqual("Generational Distance", GenerationalDistance([]).get_name())

    def test_get_short_name_return_the_right_value(self):
        self.assertEqual("GD", GenerationalDistance([]).get_short_name())

    def test_case1(self):
        """
        Case 1. Reference front: [[1.0, 1.0]], front: [[1.0, 1.0]]
        Expected result: the distance to the nearest point of the reference front is 0.0
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0]]))
        front = np.array([[1.0, 1.0]])

        result = indicator.compute(front)

        self.assertEqual(0.0, result)

    def test_case2(self):
        """
        Case 2. Reference front: [[1.0, 1.0], [2.0, 2.0], front: [[1.0, 1.0]]
        Expected result: the distance to the nearest point of the reference front is 0.0
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0], [2.0, 2.0]]))
        front = np.array([[1.0, 1.0]])

        result = indicator.compute(front)

        self.assertEqual(0.0, result)

    def test_case3(self):
        """
        Case 3. Reference front: [[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]], front: [[1.0, 1.0, 1.0]]
        Expected result: the distance to the nearest point of the reference front is 0.0. Example with three objectives
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]))
        front = np.array([[1.0, 1.0, 1.0]])

        result = indicator.compute(front)

        self.assertEqual(0.0, result)

    def test_case4(self):
        """
        Case 4. reference front: [[1.0, 1.0], [2.0, 2.0]], front: [[1.5, 1.5]]
        Expected result: the distance to the nearest point of the reference front is the euclidean distance to any of the
        points of the reference front
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0], [2.0, 2.0]]))
        front = np.array([[1.5, 1.5]])

        result = indicator.compute(front)

        self.assertEqual(np.sqrt(pow(1.0 - 1.5, 2) + pow(1.0 - 1.5, 2)), result)
        self.assertEqual(np.sqrt(pow(2.0 - 1.5, 2) + pow(2.0 - 1.5, 2)), result)

    def test_case5(self):
        """
        Case 5. reference front: [[1.0, 1.0], [2.1, 2.1]], front: [[1.5, 1.5]]
        Expected result: the distance to the nearest point of the reference front is the euclidean distance
        to the nearest point of the reference front ([1.0, 1.0])
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0], [2.1, 2.1]]))
        front = np.array([[1.5, 1.5]])

        result = indicator.compute(front)

        self.assertEqual(np.sqrt(pow(1.0 - 1.5, 2) + pow(1.0 - 1.5, 2)), result)
        self.assertEqual(np.sqrt(pow(2.0 - 1.5, 2) + pow(2.0 - 1.5, 2)), result)

    def test_case6(self):
        """
        Case 6. reference front: [[1.0, 1.0], [2.1, 2.1]], front: [[1.5, 1.5], [2.2, 2.2]]
        Expected result: the distance to the nearest point of the reference front is the average of the sum of each point
        of the front to the nearest point of the reference front
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0], [2.1, 2.1]]))
        front = np.array([[1.5, 1.5], [2.2, 2.2]])

        result = indicator.compute(front)
        distance_of_first_point = np.sqrt(pow(1.0 - 1.5, 2) + pow(1.0 - 1.5, 2))
        distance_of_second_point = np.sqrt(pow(2.1 - 2.2, 2) + pow(2.1 - 2.2, 2))

        self.assertEqual((distance_of_first_point + distance_of_second_point) / 2.0, result)

    def test_case7(self):
        """
        Case 7. reference front: [[1.0, 1.0], [2.1, 2.1]], front: [[1.5, 1.5], [2.2, 2.2], [1.9, 1.9]]
        Expected result: the distance to the nearest point of the reference front is the sum of each point of the front to the
        nearest point of the reference front
        :return:
        """
        indicator = GenerationalDistance(np.array([[1.0, 1.0], [2.1, 2.1]]))
        front = np.array([[1.5, 1.5], [2.2, 2.2], [1.9, 1.9]])

        result = indicator.compute(front)
        distance_of_first_point = np.sqrt(pow(1.0 - 1.5, 2) + pow(1.0 - 1.5, 2))
        distance_of_second_point = np.sqrt(pow(2.1 - 2.2, 2) + pow(2.1 - 2.2, 2))
        distance_of_third_point = np.sqrt(pow(2.1 - 1.9, 2) + pow(2.1 - 1.9, 2))

        self.assertEqual((distance_of_first_point + distance_of_second_point + distance_of_third_point) / 3.0, result)

