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
    assert fibonacci(1) == 1  # Updated to expect 1 for fibonacci(1)
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_fibonacci_zero():
    assert fibonacci(0) == 0

def test_fibonacci_negative():
    try:
        fibonacci(-1)
    except ValueError as e:
        assert str(e) == "n must be a non-negative integer"

def test_fibonacci_array():
    a = np.array([0, 1, 2, 3, 4, 5])
    expected = np.array([0, 1, 1, 2, 3, 5])
    assert np.array_equal(fibonacci(a), expected)

def test_fibonacci_array_negative():
    a = np.array([0, 1, -2, 3, 4, 5])
    try:
        fibonacci(a)
    except ValueError as e:
        assert str(e) == "All elements in the array must be non-negative integers"
