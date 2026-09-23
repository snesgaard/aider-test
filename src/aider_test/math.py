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
    
    def fib_single(x):
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, x + 1):
                a, b = b, a + b
            return b
    
    result = np.vectorize(fib_single)(n)
    return result
