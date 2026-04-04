import pytest
from math_utils import add, divide

def test_add_integers():
    assert add(2, 3) == 5  # returns 6 — FAIL

def test_add_negative():
    assert add(-1, 1) == 0  # returns 1 — FAIL

def test_divide_normal():
    assert divide(10, 2) == 5.0  # passes

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)  # passes
