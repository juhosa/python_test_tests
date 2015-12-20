import unittest
from codes.stuffs import some_fancy_math_func2


class TestTSFM2(unittest.TestCase):
    def setUp(self):
        pass

    def test_success_4(self):
        self.assertEqual(some_fancy_math_func2(4), 1.0)

    def test_success_5(self):
        self.assertEqual(some_fancy_math_func2(5), 8.0)

    def test_fail_6(self):
        self.assertNotEqual(some_fancy_math_func2(6), 123)