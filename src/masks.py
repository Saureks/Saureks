# import widget


def card_numbers_encryption(card: [int]) -> None:
    """принимает на вход номер карты и возвращает ее маску"""
    card_number = card.split()[-1]
    card_name = card.split()[-2]
    print(card_number)
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    print(card_name + " ".join([private_number[i: i + chunk_size] for i in range(0, chunks, chunk_size)]))
    return


# print(card_numbers_encryption(widget.card_or_account(card)))


def get_hide(cards: [int]) -> None:
    """принимает на вход номер счёта и возвращает его маску"""
    hided_num = "*" * len(cards[:2]) + cards[-4:]
    card_name = cards.split()[-2]
    return print(card_name + hided_num)


# print(get_hide(widget.card_or_account(cards)))
