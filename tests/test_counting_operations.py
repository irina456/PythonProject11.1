from src.counting_operations import counting_operations


def test_conversion_json_to_object_ok(input_list_operation_to_count, type_operation_dict):
    assert counting_operations(input_list_operation_to_count, type_operation_dict) == {
        "Перевод со счета на счет": 8,
        "Перевод с карты на карту": 47,
        "Перевод организации": 5,
        "Открытие вклада": 2,
    }
