from summary.sum1.login_button import LoginButton
import pytest


@pytest.fixture
def checker():
    return LoginButton()


def test_login_button(checker):
    assert checker.get_label() == "Login"


