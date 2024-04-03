from utils2 import mult
from utils2 import div


def test_mult():
    assert mult(1, 2) == 2
    assert mult(5, 5) == 25
    assert mult(3, 4) == 12


def test_div():
    assert div(2, 1) == 2
    assert div(6, 2) == 3
    assert div(6, 3) == 2