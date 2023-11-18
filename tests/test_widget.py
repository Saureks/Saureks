import pytest
from src.widget import card_or_account, get_data


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("счет 12345678901234567890", "счет **7890"),
        ("visa 1234567890123456", "visa 1234 56** **** 3456"),
        ("visa card 1234567890123456", "visa card 1234 56** **** 3456"),
    ],
)
def test_card_or_account(n, expected_result):
    assert card_or_account(n) == expected_result


@pytest.mark.parametrize("n, expected_result", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_get_data(n, expected_result):
    assert get_data(n) == expected_result
