from fuel import convert, gauge

import pytest

# Testes para convert

def test_convert_valid():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("5/5") == 100
    assert convert("0/5") == 0


def test_rounding():
    # 1/3 ≈ 33.3 → arredonda para 33
    assert convert("1/3") == 33
    # 2/3 ≈ 66.6 → arredonda para 67
    assert convert("2/3") == 67


def test_valueerror():
    with pytest.raises(ValueError):
        convert("cat/egg")

    with pytest.raises(ValueError):
        convert("-5/4")


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("10/0")

# ----------------------------

# Testes para gauge
def test_gauge_empty_full():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"


