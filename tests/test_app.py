import pytest
#from addition import add  # Import the add function from app.py

def add(a, b):
    return a + b

def test_add():
    # Test normal addition
    assert add(1, 2) == 3
    
    # Test addition with negative numbers
    assert add(1, -1) == 0
    assert add(-1, -1) == -2
    
    # Test adding zero
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5
    
    # Test adding large numbers
    assert add(1000000, 2000000) == 3000000
