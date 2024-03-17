import numpy as np
from matrix2d import Matrix2D

np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

with open('artifacts/3_1/matrix+.txt', 'w') as f:
    f.write(str(Matrix2D.from_numpy(a) + Matrix2D.from_numpy(b)))

with open('artifacts/3_1/matrix*.txt', 'w') as f:
    f.write(str(Matrix2D.from_numpy(a) * Matrix2D.from_numpy(b)))

with open('artifacts/3_1/matrix@.txt', 'w') as f:
    f.write(str(Matrix2D.from_numpy(a) @ Matrix2D.from_numpy(b)))
