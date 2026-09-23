import numpy as np
from typing import Union

def multiply(a: Union[int, np.ndarray], b: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """
    Multiplies two numbers or numpy arrays element-wise.
    """
    return a * b

def add(a: Union[int, np.ndarray], b: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """
    Adds two numbers or numpy arrays element-wise.
    """
    return a + b

def subtract(a: Union[int, np.ndarray], b: Union[int, np.ndarray]) -> Union[int, np.ndarray]:
    """
    Subtracts two numbers or numpy arrays element-wise.
    """
    return a - b
