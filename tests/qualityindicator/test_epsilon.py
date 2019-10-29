import unittest

from mootils.qualityindicator.epsilon import EpsilonIndicator


class EpsilonIndicatorTestCases(unittest.TestCase):

    def test_should_constructor_create_a_non_null_object(self) -> None:
        indicator = EpsilonIndicator([])
        self.assertIsNotNone(indicator)



if __name__ == '__main__':
    unittest.main()
