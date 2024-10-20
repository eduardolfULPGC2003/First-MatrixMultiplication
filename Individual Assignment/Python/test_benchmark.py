import pytest
import random
from time import *

def matrix_multiplication(x):
    A = [[random.random() for _ in range(x)] for _ in range(x)]
    B = [[random.random() for _ in range(x)] for _ in range(x)]
    C = [[0 for _ in range(x)] for _ in range(x)]
    
    for i in range(x):
        for j in range(x):
            for k in range(x):
                C[i][j] += A[i][k] * B[k][k]
    return C

@pytest.mark.parametrize("sizes", [
    1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024
])

def test_my_function(benchmark, sizes):
    result = benchmark.pedantic(matrix_multiplication, args=(sizes,), iterations=5, rounds=3)