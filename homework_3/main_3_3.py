from matrix2d import Matrix2D

a = Matrix2D([[1, 2], [3, 4]])
b = Matrix2D([[5, 6], [7, 8]])
c = Matrix2D([[3, 4], [1, 2]])
d = Matrix2D([[5, 6], [7, 8]])

with open('artifacts/3_3/A.txt', 'w') as f:
    f.write(str(a))

with open('artifacts/3_3/B.txt', 'w') as f:
    f.write(str(b))

with open('artifacts/3_3/C.txt', 'w') as f:
    f.write(str(c))

with open('artifacts/3_3/D.txt', 'w') as f:
    f.write(str(d))

with open('artifacts/3_3/AB.txt', 'w') as f:
    f.write(str(a * b))

with open('artifacts/3_3/CD.txt', 'w') as f:
    f.write(str(c * d))

with open('artifacts/3_3/hash.txt', 'w') as f:
    f.write(str(hash(a * b)) + '\n')
    f.write(str(hash(c * d)) + '\n')
