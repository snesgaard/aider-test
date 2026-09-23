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
    Computes the n-th Fibonacci number, starting from 0.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
