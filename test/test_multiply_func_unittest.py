import unittest
from codes.stuffs import multiply_func


class TestMF(unittest.TestCase):
    def setUp(self):
        pass

    def test_3_4(self):
        self.assertEqual(multiply_func(3,4), 12)

    def test_3_a(self):
        self.assertEqual(multiply_func(3, 'a'), 'aaa')


if __name__ == '__main__':
    unittest.main()
