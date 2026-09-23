import numpy as np

from aider_test.math import add, fibonacci, multiply, subtract


def test_multiply_integers():
    assert multiply(2, 3) == 6

def test_multiply_arrays():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert np.array_equal(multiply(a, b), np.array([4, 10, 18]))

def test_add_integers():
    assert add(2, 3) == 5

def test_add_arrays():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    assert np.array_equal(add(a, b), np.array([5, 7, 9]))

def test_subtract_integers():
    assert subtract(5, 3) == 2

def test_subtract_arrays():
    a = np.array([5, 7, 9])
    b = np.array([4, 5, 6])
    assert np.array_equal(subtract(a, b), np.array([1, 2, 3]))

def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(10) == 34
