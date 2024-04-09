from utils import add  # importing the function add from the file utils
from utils import substract  # importing the function substract from the file utils


def test_add():  # defining a test function to test the function add
    assert add(1, 2) == 3
    assert add(5, 5) == 12
    assert add(3, 4) == 7


def test_substract():  # defining a test function to test the function substract
    assert substract(2, 1) == 1
    assert substract(5, 2) == 4
    assert substract(6, 3) == 3
