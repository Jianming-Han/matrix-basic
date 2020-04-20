# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from matrix_basic import Matrix


class TestMatrixcalClass(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix()

    def test_add(self):
        arr1 = [[1, 2, 3], [4, 5, 6]]
        arr2 = [[1, 1, 1], [1, 1, 1]]
        arr3 = [[2, 3, 4], [5, 6, 7]]
        self.assertEqual(self.matrix.add(arr1, arr2), arr3, 'add matrices not as expected')

    def test_subtract(self):
        arr1 = [[1, 2, 3], [4, 5, 6]]
        arr2 = [[1, 1, 1], [1, 1, 1]]
        arr3 = [[2, 3, 4], [5, 6, 7]]
        self.assertEqual(self.matrix.subtract(arr3, arr1), arr2, 'subtract matrices not as expected')

    def test_multiply(self):
        arr1 = [[1, 2, 3], [4, 5, 6]]
        arr2 = [[2, 1], [1, 1], [1, 1]]
        arr3 = [[7, 6], [19, 15]]
        self.assertEqual(self.matrix.multiply(arr1, arr2), arr3, 'multiply matrices not as expected')

    def test_transpose(self):
        arr1 = [[1, 2, 3], [4, 5, 6]]
        arr2 = [[1, 4], [2, 5], [3, 6]]
        self.assertEqual(self.matrix.transpose(arr1), arr2, 'transpose matrix not as expected')


if __name__ == '__main__':
    unittest.main()