import src.masks


def card_or_account():
    info = input("Введите данные карты или счета: ").lower()
    num = info.find("счет")
    print(num)
    if num == 0:
        cards = info
        return src.masks.get_hide(cards)
    else:
        card = info
        return src.masks.card_numbers_encryption(card)
