

def card_numbers_encryption(card: [int]) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    card_number = card.split()[-1]
    private_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    chunks, chunk_size = len(private_number), len(private_number) // 4
    return " ".join([private_number[i: i + chunk_size] for i in range(0, chunks, chunk_size)])


print(card_numbers_encryption(input("Введите номер карты")))


def get_hide(card: [int]) -> str:
    """принимает на вход номер счёта и возвращает его маску"""
    hided_num = "*" * len(card[:2]) + card[-4:]
    return hided_num


print(get_hide(input("Введите номер счета")))
