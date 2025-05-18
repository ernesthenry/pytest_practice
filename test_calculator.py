import pytest
from .calculator import add, subtract, multiply, divide


def test_add():
    assert add(1,3) == 4
    assert add(-1,1) == 0
    assert add(-1,-1) == -2
    assert add(0,0) == 0

def test_subtract():
    assert subtract(3,1) == 2
    assert subtract(1,1) == 0

def test_multiply():
    assert multiply(3,1) ==3
    assert multiply(0,1) == 0
    assert multiply(-1,1) == -1
    assert multiply(-1,-1) == 1

def test_divide():
    assert divide(6,2) == 3
    


def divide_by_zero():
    # with pytest.raises(ValueError):
    #     divide(1,0)                    
    with pytest.raises(ZeroDivisionError):
        divide(2/0)