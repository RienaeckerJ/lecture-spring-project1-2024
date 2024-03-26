from utils import add
from utils import substract
def test_add():
    assert add(1,2) == 3
    assert add(5,5) == 10
    assert add(3,4) == 7

def test_substract():
    assert substract(2, 1) == 1
    assert substract(5, 2) == 3
    assert substract(6, 3) == 3