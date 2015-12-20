import unittest
from codes.stuffs import return_str

class TestSubStr(unittest.TestCase):
    string = ''
    result = ''

    def setUp(self):
        self.string = 'this_is_a_string'
        self.result = 'this'

    def test_substr(self):
        self.assertEqual(return_str(self.string, 4), self.result)
