import unittest
from codes.stuffs import return_str


class TestSubStr(unittest.TestCase):
    string = ''
    result = ''

    def setUp(self):
        self.string = 'this_is_a_string'
        self.result = 'this'

    def test_substr_success(self):
        self.assertEqual(return_str(self.string, 4), self.result)

    def test_substr_fail(self):
        self.assertNotEqual(return_str(self.string, 6), self.result)
