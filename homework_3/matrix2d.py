from typing import List, Union, Tuple
import numpy as np  # использую  только для тестов


def cache_this(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            res = func(*args)
            cache[args] = res
            return res

    return wrapper


class SumHashingMixin:
    def __hash__(self):
        return sum(sum(row) for row in self._matrix) # хэш матрицы - ее сумма


class Matrix2D(SumHashingMixin):
    def __init__(self, lists: List[List[Union[float, int]]]):
        assert all(len(row) == len(lists[0]) for row in lists)

        self._matrix = lists
        self._dtype = type(lists[0][0])

    @property
    def shape(self) -> (int, int):
        return len(self._matrix), len(self._matrix[0])

    def transpose(self):
        return Matrix2D([[row[i] for row in self._matrix] for i in range(len(self._matrix[0]))])

    def to_numpy(self) -> np.ndarray:
        return np.array(self._matrix)

    @classmethod
    def from_numpy(cls, np_array: np.ndarray):
        return cls(np_array.tolist())

    def __getitem__(self, indices: Union[Tuple[int, int], int]):
        if isinstance(indices, int):
            return self._matrix[indices]
        elif isinstance(indices, tuple):
            row_idx, col_idx = indices
            return self._matrix[row_idx][col_idx]
        raise IndexError

    def __setitem__(self, indices: Union[Tuple[int, int], int], value: Union[float, int, List[Union[float, int]]]):
        if isinstance(indices, int):
            self._matrix[indices] = value
        elif isinstance(indices, tuple):
            row_idx, col_idx = indices
            self._matrix[row_idx][col_idx] = value
        else:
            raise IndexError(f'Got {indices} of type {type(indices)}')

    @cache_this
    def __add__(self, other) -> 'Matrix2D':
        assert self.shape == other.shape, f'Shapes do not match: left shape: {self.shape}, right shape: {other.shape}'

        return Matrix2D([[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self._matrix, other._matrix)])

    @cache_this
    def __matmul__(self, other) -> 'Matrix2D':
        assert self.shape[1] == other.shape[0], f'Shapes do not match: left shape: {self.shape}, right shape: {other.shape}'

        resulting_matrix = Matrix2D([[0 for _ in range(other.shape[1])] for _ in range(self.shape[0])])

        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                resulting_matrix[i, j] = sum(self[i, k] * other[k, j] for k in range(self.shape[1]))

        return resulting_matrix

    @cache_this
    def __mul__(self, other) -> 'Matrix2D':
        assert self.shape == other.shape, f'Shapes do not match: left shape: {self.shape}, right shape: {other.shape}'

        return Matrix2D([[a * b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(self._matrix, other._matrix)])

    def __str__(self) -> str:
        s = "\n          ".join([str(row) for row in self._matrix])
        return f'Matrix2D([{s}])'

