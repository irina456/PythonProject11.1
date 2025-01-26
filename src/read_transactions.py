import pandas as pd
from pandas import DataFrame


def get_read_csv(path_to_file: str) -> DataFrame | str:
    """
    Считывание данных о финансовых операциях из CSV-файла.

    :param path_to_file: Путь к CSV файлу, который необходимо считать.
    :return: Первые пять строк данных в формате JSON, или сообщение об ошибке.
    """
    try:
        # Чтение данных из CSV файла с указанным разделителем
        data_transactions = pd.read_csv(path_to_file, delimiter=";")

    except FileNotFoundError as exc_info:
        # Возврат сообщения об ошибке, если файл не найден
        return f"Function {get_read_csv.__name__} error: {type(exc_info).__name__}"
    except Exception as exc_info:
        # Возврат сообщения об общей ошибке
        return f"Error: {type(exc_info).__name__} - {str(exc_info)}"

    else:
        # Возврат первых пяти строк в формате JSON
        return data_transactions.head().to_json(orient="records", indent=4, lines=True, force_ascii=False)


def get_read_excel(path_to_file: str) -> str | list[dict]:
    """
    Считывание данных о финансовых операциях из файла Excel.

    :param path_to_file: Путь к Excel файлу, который необходимо считать.
    :return: Список словарей с первыми пятью строками данных, или сообщение об ошибке.
    """
    try:
        # Чтение данных из Excel файла
        data_transactions = pd.read_excel(path_to_file)

    except FileNotFoundError as exc_info:
        # Возврат сообщения об ошибке, если файл не найден
        return f"Function {get_read_excel.__name__} error: {type(exc_info).__name__}"
    except Exception as exc_info:
        # Возврат сообщения об общей ошибке
        return f"Error: {type(exc_info).__name__} - {str(exc_info)}"

    else:
        # Возврат первых пяти строк в виде списка словарей
        return data_transactions.head().to_dict(orient="records")