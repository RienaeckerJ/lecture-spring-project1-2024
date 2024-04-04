from utils2 import mult  # importing the function mult from the file utils2
from utils2 import div  # importing the function div from the file utils2


def test_mult():  # defining a test function to test the function mult
    assert mult(1, 2) == 2
    assert mult(5, 5) == 25
    assert mult(3, 4) == 12


def test_div():  # defining a test function to test the function div
    assert div(2, 1) == 2
    assert div(6, 2) == 3
    assert div(6, 3) == 2
