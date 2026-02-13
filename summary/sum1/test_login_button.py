from summary.sum1.login_button import LoginButton
import pytest


@pytest.fixture
def checker():
    return LoginButton()


def test_login_button(checker):
    assert checker.get_label() == "Login"


def test_button_is_enable_by_default(checker):
    assert checker.is_enabled() is True


def test_button_is_disabled(checker):
    checker.disable()
    assert checker.is_enabled() is False


def test_button_status_chek(checker):
    checker.disable()
    checker.enable()
    assert checker.is_enabled() is True