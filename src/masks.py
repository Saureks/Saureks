def card_numbers_encryption(number_card: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    mask_card = number_card[0:4] + " " + number_card[4:6] + "** ****" + " " + number_card[-4:]
    return mask_card


def get_account(account_mask: str) -> str:
    """принимает на вход номер счёта и возвращает его маску"""
    mask_account = "**" + account_mask[-4:]
    return mask_account
