from utils import add

def test_add():
    assert add(1,2) == 3
    assert add(5,5) == 10
    assert add(3,4) == 7

def test_substract():
    assert substract(x:2, y:1) == 1
    assert substract(x:5, y:2) == 3
    assert substract(x:6, y:3) == 3