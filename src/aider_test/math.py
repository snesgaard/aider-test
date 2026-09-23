import numpy as np


def multiply(a: int | np.ndarray, b: int | np.ndarray) -> int | np.ndarray:
    """
    Multiplies two numbers or numpy arrays element-wise.
    """
    return a * b

def add(a: int | np.ndarray, b: int | np.ndarray) -> int | np.ndarray:
    """
    Adds two numbers or numpy arrays element-wise.
    """
    return a + b

def subtract(a: int | np.ndarray, b: int | np.ndarray) -> int | np.ndarray:
    """
    Subtracts two numbers or numpy arrays element-wise.
    """
    return a - b

def fibonacci(n: int) -> int:
    """
    Computes the n-th Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
