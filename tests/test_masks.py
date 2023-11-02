import pytest

from src.masks import card_numbers_encryption, get_account


@pytest.mark.parametrize("n, expected_result", [("1234567890123456", "1234 56** **** 3456")])
def test_card_numbers_encryption(n, expected_result):
    assert card_numbers_encryption(n) == expected_result


@pytest.mark.parametrize("n, expected_result", [("12345678901234567890", "**7890")])
def test_get_account(n, expected_result):
    assert get_account(n) == expected_result
