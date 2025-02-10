import logging
from collections import Counter


logger_counting = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s \n%(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_counting.addHandler(file_handler)
logger_counting.setLevel(logging.INFO)


# type_operation_dict = {
#     "Перевод со счета на счет": 0,
#     "Перевод с карты на карту": 0,
#     "Перевод организации": 0,
#     "Открытие вклада": 0,
# }


def counting_operations(list_operation: list[dict] = [], operatin_type: dict = {}) -> dict:
    count_list = []
    for i, operat in enumerate(list_operation):
        count_list.append(operat["description"])
    logger_counting.info(f"Resul: {count_list}")
    counted = dict(Counter(count_list))

    for i, types in enumerate(counted):
        if types in operatin_type:
            operatin_type[types] = counted[types]

    logger_counting.info(f"Resul: {operatin_type}")
    return operatin_type
