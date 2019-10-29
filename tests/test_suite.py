import os
import unittest

loader = unittest.TestLoader()
folder = os.path.dirname(os.path.realpath(__file__))

suite = loader.discover(folder)

runner = unittest.TextTestRunner()
ret = unittest.TextTestRunner().run(suite)

if len(ret.failures) + len(ret.errors) > 0:
    exit(1)
