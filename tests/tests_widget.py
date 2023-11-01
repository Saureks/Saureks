import pytest
from src.widget import card_or_account, get_data



@pytest.mark.parametrize("n, expected_result", [("счет 12345678901234567890", "счет **7890")])
def card_or_account(n, expected_result):
    assert n == expected_result

@pytest.mark.parametrize("n, expected_result", [("visa 1234567890123456", "счет 1234 56** **** 3456")])
def card_or_account(n, expected_result):
    assert n == expected_result


