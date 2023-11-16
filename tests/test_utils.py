import pytest

from config import DATA_PATH_TEST
from src.utils import get_operations, get_json_file


@pytest.fixture()
def test_dicts():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


def test_get_operations(test_dicts):
    with pytest.raises(ValueError):
        assert get_operations(test_dicts[1]) == "Транзация выполнена не в рублях. Укажите транзакцию в рублях"


def test_get_operations_rub(test_dicts):
    assert get_operations(test_dicts[0]) == 31957.58


def test_get_json_file():
    assert get_json_file(DATA_PATH_TEST) == []
