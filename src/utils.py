import json
import logging
from json import JSONDecodeError
from typing import Any

utils_logger = logging.getLogger("app.get_read_file")
main_utils_logger = logging.getLogger("app.main_read")
file_handler = logging.FileHandler("./logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
main_utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)
main_utils_logger.setLevel(logging.DEBUG)


def get_read_file(path_to_file: str) -> str | list[dict] | Any:

    """
    Принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях
    :param path_to_file:
    :return:
    """
    try:
        with open(path_to_file, encoding="utf-8") as file:
            try:
                operations_data = json.load(file)

            except JSONDecodeError:
                print("JSONDecodeError: Invalid JSON data.")
                return []

    except FileNotFoundError:
        print("FileNotFoundError: Файл не найден.")
        return []

    return operations_data
