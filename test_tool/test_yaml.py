import pytest


def ma(i):
    a = i + 1
    return a


def test_ma():
    assert ma(1) == 2


if __name__ == '__main__':
    pytest.main()
