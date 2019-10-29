import os
import unittest

loader = unittest.TestLoader()
folder = os.path.dirname(os.path.realpath(__file__))

suite = loader.discover(folder)

runner = unittest.TextTestRunner()
runner.run(suite)