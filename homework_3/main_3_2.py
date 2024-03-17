import numpy as np
from matrix2d_mixins import Matrix2DMixins

np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

(Matrix2DMixins(a) + Matrix2DMixins(b)).write_to_file('artifacts/3_2/matrix+.txt')
(Matrix2DMixins(a) * Matrix2DMixins(b)).write_to_file('artifacts/3_2/matrix*.txt')
(Matrix2DMixins(a) @ Matrix2DMixins(b)).write_to_file('artifacts/3_2/matrix@.txt')
