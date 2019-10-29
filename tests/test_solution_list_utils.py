import unittest

from numpy.testing import assert_raises
from mootils.util.solution_list_utils import read_solutions_from_file


class SolutionListUtilsTestCases(unittest.TestCase):

    def test_should_read_solutions_from_file_read_an_existing_file_with_a_2D_front(self) -> None:
        front = read_solutions_from_file("../resources/paretofronts/ZDT1.pf")

        self.assertIsNotNone(front)

        number_of_objectives = 2
        self.assertEquals(number_of_objectives, front[0].size)

    def test_should_read_solutions_from_file_read_an_existing_file_with_a_3D_front(self) -> None:
        front = read_solutions_from_file("../resources/paretofronts/DTLZ2.3D.pf")

        self.assertIsNotNone(front)

        number_of_objectives = 3
        self.assertEquals(number_of_objectives, front[0].size)

    def test_should_read_solutions_from_file_fails_if_the_file_does_not_exist(self) -> None:
        with assert_raises(IOError):
            read_solutions_from_file("../resources/paretofronts/xxxxx.pf")


if __name__ == '__main__':
    unittest.main()
