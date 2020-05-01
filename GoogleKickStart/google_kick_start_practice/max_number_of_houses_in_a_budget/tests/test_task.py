import unittest

from ..max_number_of_houses_in_a_budget import get_max_number_of_houses


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_get_max_number_of_houses(self):
        self.assertEqual(get_max_number_of_houses([2000,500,500,500,500], 1000), 2, msg="maximum 2 houses can be "
                                                                                        "purchased in the budget 1000"
                                                                                        "from the given house prices "
                                                                                        "[2000,500,500,500,500]")
