import pytest

from src.file_interpretation import conversion_csv_to_object, conversion_xlsx_to_object


def test_conversion_csv_to_object_path():
    assert len(conversion_csv_to_object("data/transactions.csv")) == 1000


@pytest.mark.parametrize(
    "key, expected",
    [
        ("", []),
        (None, []),
        (12456, []),
    ],
)
def test_conversion_csv_to_object_no_valid(key, expected):
    assert conversion_csv_to_object(key) == expected


def test_conversion_xlsx_to_object_path():
    assert len(conversion_xlsx_to_object("data/transactions_excel.xlsx")) == 1000


@pytest.mark.parametrize(
    "key, expected",
    [
        ("", []),
        (None, []),
        (12456, []),
    ],
)
def test_conversion_xlsx_to_object_no_valid(key, expected):
    assert conversion_xlsx_to_object(key) == expected
