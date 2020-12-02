"""Tests function implementation"""
import pytest
from factorial import factorial


def test_basic_behavior():
    """test basic behavior"""
    # n! =n x (n-1) x ... 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(10) == 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

def test_extreme_cases():
    """Extreme cases"""
    with pytest.raises(ValueError):
        assert factorial(10000000000000000)
    with pytest.raises(TypeError):
        assert factorial(0.5)
    with pytest.raises(TypeError):
        assert factorial('a')
    with pytest.raises(ValueError):
        assert factorial(-1)
