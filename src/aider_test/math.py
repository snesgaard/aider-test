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

def fibonacci(n: int | np.ndarray) -> int | np.ndarray:
    """
    Computes the n-th Fibonacci number or Fibonacci sequence for a numpy array of indices.
    """
    if isinstance(n, int):
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
    elif isinstance(n, np.ndarray):
        if not np.issubdtype(n.dtype, np.integer) or (n < 0).any():
            raise ValueError("All elements in the array must be non-negative integers")
        result = np.zeros_like(n, dtype=int)
        for i in range(n.size):
            result[i] = fibonacci(n[i])
        return result
    else:
        raise TypeError("Input must be an integer or a numpy array of integers")
