from summary.sum1.age import AgeValidator
import pytest


@pytest.fixture
def checker():
    return AgeValidator()


def test_age(checker):
    assert checker.is_adult(17) is False


def test_is_adult(checker):
    assert checker.is_adult(18) is True


def test_adult(checker):
    assert checker.is_adult(19) is True