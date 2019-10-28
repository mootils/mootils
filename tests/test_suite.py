import unittest

# initialize the test suite
from tests.test_quality_indicator import GenerationalDistanceTestCases, InvertedGenerationalDistanceTestCases, \
    EpsilonIndicatorTestCases

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(GenerationalDistanceTestCases))
suite.addTests(loader.loadTestsFromModule(InvertedGenerationalDistanceTestCases))
suite.addTests(loader.loadTestsFromModule(EpsilonIndicatorTestCases))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
