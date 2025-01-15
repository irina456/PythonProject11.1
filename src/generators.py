from typing import Generator


def filter_by_currency(transactions: list, currency: str = "USD") -> Generator:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)"""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction  # Теперь возвращает один словарь вместо списка


def transaction_descriptions(transactions: list) -> Generator:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой поочередно"""

    for description in transactions:
        yield description["description"]  # Поочередно выдает описание транзакции


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерирует номера банковских карт в заданном диапазоне
    в формате 'ХХХХ ХХХХ ХХХХ ХХХХ'"""

    if isinstance(start, int) and isinstance(stop, int):  # Проверка типов
        for number in range(start, stop + 1):  # Включая правую границу
            number_card = "0" * (16 - len(str(number))) + str(number)  # Формирование числа из 16 символов
            yield f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"  # Обратите внимание на последние 4 цифры
    else:  # Если значения старт и стоп не числа
        yield "Ошибка: некорректный ввод"