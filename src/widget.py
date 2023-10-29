import re

from src.masks import card_numbers_encryption, get_account


def card_or_account(word: str) -> str:
    """
    принимает на вход строку информацией тип карты/счета и номер карты/счета
    """
    card_list = word.split(" ")
    name = " ".join(card_list[:-1])
    if "счет" in name.lower():
        masked_number = get_account(card_list[-1])
        return name + " " + masked_number
    else:
        masked_card = card_numbers_encryption(card_list[-1])
        return name + " " + masked_card


def get_data(data: str) -> str:
    """
    принимает на вход строку,
    вида "2018-07-11T02:26:18.671407" и
    возвращает строку с датой в виде "11.07.2018"

    """
    data_list = re.split('T|-', data)
    data_form = data_list[-2] + "." + data_list[-3] + "." + data_list[-4]
    return data_form
