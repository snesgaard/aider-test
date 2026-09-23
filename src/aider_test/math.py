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

def fibonacci(n: int | np.ndarray) -> np.ndarray:
    """
    Computes the n-th Fibonacci number or Fibonacci sequence for a numpy array of indices.
    """
    if isinstance(n, int):
        n = np.array([n])
    
    if not np.issubdtype(n.dtype, np.integer) or (n < 0).any():
        raise ValueError("n must be a non-negative integer")
    
    result = np.zeros_like(n, dtype=int)
    for i in range(n.size):
        if n[i] == 0:
            result[i] = 0
        elif n[i] == 1:
            result[i] = 1
        else:
            a, b = 0, 1
            for _ in range(2, n[i] + 1):
                a, b = b, a + b
            result[i] = b
    
    return result
