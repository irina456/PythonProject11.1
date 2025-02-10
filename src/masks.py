import logging

logger_masks = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_masks.addHandler(file_handler)
logger_masks.setLevel(logging.INFO)


# Functional part
def get_mask_card_number(card_number: str = "", start: int = 0) -> str:
    """принимает на вход номер карты, индекс первой цыфры номера карты и возвращает маску номера
    по правилу User Name XXXX XX** **** XXXX"""
    logger_masks.info("Get started get_mask_card_number")
    out_format = card_number[:start]
    split = start + 3
    temp = range(start + 6, start + 12)

    for i in range(len(card_number)):
        if i >= start:
            if i in temp:
                out_format += "*"
                if i != len(card_number) - 1:
                    if i == split:
                        out_format += " "
                        split += 4
            else:
                out_format += card_number[i]
                if i != len(card_number) - 1:
                    if i == split:
                        out_format += " "
                        split += 4

    if card_number == "":
        logger_masks.warning(f'''Возвращаем пустую строку, на вход получили: "{card_number}"''')
        return ""
    else:
        return out_format


def get_mask_account(bank_account: str = "", start: int = 0) -> str:
    """принимает на вход номер счета и возвращает маску номера по правилу Name **XXXX"""
    logger_masks.info("Get started get_mask_account")
    out_format = ""

    out_format += bank_account[:start] + "**" + bank_account[-4:]

    if bank_account == "":
        logger_masks.warning(f'''Возвращаем пустую строку, на вход получили: "{bank_account}"''')
        return ""
    else:
        return out_format
