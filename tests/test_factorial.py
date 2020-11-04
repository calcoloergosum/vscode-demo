"""Tests basic functionality"""
import pytest
from factorial import factorial


def test_factorial():
    """Test basic behavior"""
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(10) == 3628800


def test_wrong_type():
    """Test it outputs right type of error"""
    with pytest.raises(TypeError):
        assert factorial(1.5)

def test_wrong_range():
    """Test it outputs right type of error"""
    with pytest.raises(RuntimeError):
        assert factorial(-1)
