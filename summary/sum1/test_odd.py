from summary.sum1.odd import EvenOddChecker
import pytest


@pytest.fixture
def checker():
    return EvenOddChecker()


def test_is_even(checker):
    assert checker.is_even(2) is True
    assert checker.is_even(3) is False
    assert checker.is_even(-2) is True

def test_is_odd(checker):
    assert checker.is_odd(2) is False
    assert checker.is_odd(3) is True
    assert checker.is_odd(-2) is False
