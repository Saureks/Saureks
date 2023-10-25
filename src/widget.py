import masks
import re


def card_or_account():
    info = input("Введите данные карты или счета: ").lower()
    lists = (re.findall(r"[\w']+", info))
    if lists == "cчет":
        cards = info
        return masks.get_hide(cards)
    else:
        card = info
        return masks.card_numbers_encryption(card)
