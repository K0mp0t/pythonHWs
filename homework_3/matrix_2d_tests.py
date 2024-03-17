import unittest
import numpy as np
from matrix2d import Matrix2D


class TestAddFloat(unittest.TestCase):
    def test_something(self):
        a = np.random.rand(10, 10)
        b = np.random.rand(10, 10)

        np_result = a + b
        matrix2d_result = (Matrix2D.from_numpy(a) + Matrix2D.from_numpy(b)).to_numpy()

        assert np.allclose(np_result, matrix2d_result), (np_result, matrix2d_result)


class TestMulFloat(unittest.TestCase):
    def test_something(self):
        a = np.random.rand(10, 10)
        b = np.random.rand(10, 10)

        np_result = a * b
        matrix2d_result = (Matrix2D.from_numpy(a) * Matrix2D.from_numpy(b)).to_numpy()

        assert np.allclose(np_result, matrix2d_result), (np_result, matrix2d_result)


class TestMatMulFloat(unittest.TestCase):
    def test_something(self):
        a = np.random.randint(0, 10, (10, 10))
        b = np.random.randint(0, 10, (10, 10))

        np_result = a @ b
        matrix2d_result = (Matrix2D.from_numpy(a) @ Matrix2D.from_numpy(b)).to_numpy()

        assert np.allclose(np_result, matrix2d_result), (np_result, matrix2d_result)


class TestAddInt(unittest.TestCase):
    def test_something(self):
        a = np.random.randint(0, 10, (10, 10))
        b = np.random.randint(0, 10, (10, 10))

        np_result = a + b
        matrix2d_result = (Matrix2D.from_numpy(a) + Matrix2D.from_numpy(b)).to_numpy()

        assert np.allclose(np_result, matrix2d_result), (np_result, matrix2d_result)


class TestMulInt(unittest.TestCase):
    def test_something(self):
        a = np.random.randint(0, 10, (10, 10))
        b = np.random.randint(0, 10, (10, 10))

        np_result = a * b
        matrix2d_result = (Matrix2D.from_numpy(a) * Matrix2D.from_numpy(b)).to_numpy()

        assert np.allclose(np_result, matrix2d_result), (np_result, matrix2d_result)


class TestMatMulInt(unittest.TestCase):
    def test_something(self):
        a = np.random.rand(10, 10)
        b = np.random.rand(10, 10)

        np_result = a @ b
        matrix2d_result = (Matrix2D.from_numpy(a) @ Matrix2D.from_numpy(b)).to_numpy()

        assert np.allclose(np_result, matrix2d_result), (np_result, matrix2d_result)


if __name__ == '__main__':
    unittest.main()
