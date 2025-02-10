import pytest

from src.executive import executive_function_output_main
from src.utils import conversion_json_to_object
from src.file_interpretation import conversion_csv_to_object, conversion_xlsx_to_object


@pytest.mark.parametrize(
    "to_mask, mesage",
    [
        (
            conversion_json_to_object,
            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации",
        ),
        (
            conversion_csv_to_object,
            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации",
        ),
        (
            conversion_xlsx_to_object,
            "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации",
        ),
    ],
)
def test_executive_function_output_main(to_mask, mesage):
    assert executive_function_output_main(to_mask) == mesage


def test_executive_1_execudet(output_execudet_json):
    assert (
        executive_function_output_main(conversion_json_to_object, "data/operations.json", "EXECUTED")
        == output_execudet_json
    )


def test_executive_2_execudet_filt_rub(output_execudet_csv_filt_rub):
    assert (
        executive_function_output_main(
            conversion_csv_to_object, "data/transactions.csv", "EXECUTED", user_choice_rub="RUB"
        )
        == output_execudet_csv_filt_rub
    )


def test_executive_3_execudet_filt_rub(output_execudet_xlsx_filt_rub):
    assert (
        executive_function_output_main(
            conversion_xlsx_to_object, "data/transactions_excel.xlsx", "EXECUTED", user_choice_rub="RUB"
        )
        == output_execudet_xlsx_filt_rub
    )
