import unittest

from unittest import TestCase

if __name__ == '__main__':
    unittest.main()


class MyTestCase(TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
