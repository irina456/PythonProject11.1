from typing import Any, List

import pytest

from src.generators import card_number_generator, filter_by_currency
from tests.conftest import result_one, result_two


def test_filter_by_currency_fixture(filter_by_currency_verification: list) -> None:
    """Тестируем фильтрацию транзакций по валюте"""
    assert next(filter_by_currency(filter_by_currency_verification, "USD")) == result_one
    assert next(filter_by_currency(filter_by_currency_verification, "RUB")) == result_two


def test_transaction_descriptions_fixture(transaction_descriptions_verification: Any) -> None:
    """Тестируем получение описаний транзакций"""
    descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]

    for description in descriptions:
        assert next(transaction_descriptions_verification) == description


@pytest.mark.parametrize(
    "start, stop, expected_value",
    [
        (10, 15, [
            "0000 0000 0000 0010",
            "0000 0000 0000 0011",
            "0000 0000 0000 0012",
            "0000 0000 0000 0013",
            "0000 0000 0000 0014",
        ]),
        (21001, 21005, [
            "0000 0000 0002 1001",
            "0000 0000 0002 1002",
            "0000 0000 0002 1003",
            "0000 0000 0002 1004"
        ]),
        # Тестируем некорректные вводы
        (1, "5", ["Ошибка: некорректный ввод"]),
        ("r", 5, ["Ошибка: некорректный ввод"]),
        ([], [], ["Ошибка: некорректный ввод"]),
    ],
)
def test_card_number_generator(start: int, stop: Any, expected_value: List[str]) -> None:
    """Тестируем генерацию номеров карт в заданном диапазоне"""
    assert list(card_number_generator(start, stop)) == expected_value