import logging

import pandas as pd

logger_interpretation = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_interpretation.addHandler(file_handler)
logger_interpretation.setLevel(logging.INFO)


def conversion_csv_to_object(file_name=""):
    """Принимает на вход путь до файла csv, который читает и
    возвращает объект Python"""
    logger_interpretation.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "rb") as f:
            return pd.read_csv(f).to_dict("records")

    except FileNotFoundError:
        logger_interpretation.warning("File not found, return []")
        return []

    except Exception:
        logger_interpretation.warning("Exceptional error, return []")
        return []


def conversion_xlsx_to_object(file_name=""):
    """Принимает на вход путь до файла xlsx, который читает и
    возвращает объект Python"""
    logger_interpretation.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "rb") as f:
            return pd.read_excel(f).to_dict("records")

    except FileNotFoundError:
        logger_interpretation.warning("File not found, return []")
        return []

    except Exception:
        logger_interpretation.warning("Exceptional error, return []")
        return []
