import json
import logging
from typing import Any


def get_json_file(file_json: str) -> Any:
    """
    принимает на вход путь до JSON-файла
    :param file_json: path
    :return: возвращает список словарей с данными о финансовых транзакциях
    """
    logging.basicConfig(
        filename="app.log", level=logging.INFO, format="%(asctime)s - %(module)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    try:
        with open(file_json, encoding="utf-8") as data:
            operations = json.load(data)
            logger.info("JSON файл успешно загружен")
    except FileNotFoundError:
        operations = list()
        logger.error("Файл не найден")
    except json.JSONDecodeError:
        operations = list()
        logger.error("Ошибка при декодировании JSON")
    return operations


def get_operations(operation: dict) -> float | str:
    """
    принимает на вход одни транзакции
    :param operation: dict
    :return: возвращает сумму транзакций в рублях
    """
    logging.basicConfig(
        filename="app.log", level=logging.INFO, format="%(asctime)s - %(module)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    if operation["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("Транзакция выполнена в рублях")
        return float(operation["operationAmount"]["amount"])
    else:
        logger.error("Транзакция выполнена не в рублях. Укажите транзакцию в рублях ")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
