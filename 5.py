import numpy as np
n = int(input())
print()
matrix = np.array([list(map(int, input().split())) for _ in range(n)])
print()

a = matrix.transpose()
b = np.dot(matrix,a)

for row in list(zip(*b)):
    print(*row)