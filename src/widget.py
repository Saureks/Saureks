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



