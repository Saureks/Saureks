import logging

logging.basicConfig(
    filename="app.log", level=logging.INFO, format="%(asctime)s - %(module)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def card_numbers_encryption(number_card: str) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    mask_card = number_card[0:4] + " " + number_card[4:6] + "** ****" + " " + number_card[-4:]
    logger.info(f"Маска номера карты {mask_card}")
    return mask_card


def get_account(account_mask: str) -> str:
    """принимает на вход номер счёта и возвращает его маску"""
    mask_account = "**" + account_mask[-4:]
    logger.info(f"Маска номера счета {mask_account}")
    return mask_account
