import numpy as np
import unittest

from numpy.testing import assert_raises
from mootils.util.vector_utils import normalize


class VectorUtilsTestCases(unittest.TestCase):

    def test_should_normalize_raise_an_exception_if_min_and_max_values_are_equal(self) -> None:
        vector = np.array([2, 4])
        min_values = np.array([1, 1])
        max_values = np.array([2, 1])

        with assert_raises(Exception):
            normalize(vector, min_values, max_values)

    def test_should_return_the_correct_normalized_vector_case1(self) -> None:
        """
        Case 1:
          vector =[0.0, 0.5, 1.0]
          min_values = None
          max_values = None

        """
        vector = np.array([0.0, 0.5, 1.0])

        normalized_vector = normalize(vector)

        np.testing.assert_array_almost_equal(vector, normalized_vector)

    def test_should_return_the_correct_normalized_vector_case2(self) -> None:
        """
        Case 1:
          vector =[10.0, 15.0, 20.0]
          min_values = [10, 10, 10]
          max_values = [20, 20, 20

        """
        vector = np.array([10.0, 15.0, 20.0])
        min_values = np.array([10, 10, 10])
        max_values = np.array([20, 20, 20])
        normalized_vector = normalize(vector, min_values, max_values)

        np.testing.assert_array_almost_equal(np.array([0.0, 0.5, 1.0]), normalized_vector)

if __name__ == '__main__':
    unittest.main()
