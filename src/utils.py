import json
from typing import Any


def get_json_file(file_json: str) -> Any:
    """
    принимает на вход путь до JSON-файла
    :param file_json: path
    :return: возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(file_json, encoding="utf-8") as data:
            operations = json.load(data)
    except FileNotFoundError:
        operations = list()
    except json.JSONDecodeError:
        operations = list()
    return operations


def get_operations(operation: dict) -> float | str:
    """
    принимает на вход одни транзакции
    :param operation: dict
    :return: возвращает сумму транзакций в рублях
    """
    if operation["operationAmount"]["currency"]["code"] == "RUB":
        return float(operation["operationAmount"]["amount"])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
