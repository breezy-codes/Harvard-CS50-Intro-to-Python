# Lecture 5
# Program task number 3
# A program to specifically test the calculator program

import pytest
# Import the square function from calculate.py file 
from calculate import square

# A test that can be done using pytest
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")