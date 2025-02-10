from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card


def executive_function_output_main(
        function_choice,
        file_path,
        user_key,
        user_choice_date,
        user_choice_sort,
        user_choice_rub,
        user_choice_name_discription,
):
    # Проверяем и задаем значения по умолчанию
    user_choice_date = user_choice_date if user_choice_date in ["да", "нет"] else "нет"
    user_choice_rub = user_choice_rub if user_choice_rub in ["да", "нет"] else "нет"
    user_choice_name_discription = user_choice_name_discription if user_choice_name_discription in ["да",
                                                                                                    "нет"] else "нет"

    # Проверка выбора сортировки
    if user_choice_sort in ["по возрастанию", "по убыванию"]:
        is_descending = user_choice_sort == "по убыванию"
    else:
        is_descending = False  # значение по умолчанию

    # Обработка файлов
    if file_path in ["data/operations.json", "data/transactions_excel.xlsx"]:
        # Применяем фильтрацию и сортировку
        filtered_data = filter_by_state(function_choice(file_path), user_key)
        return sort_by_date(filtered_data, is_descending)
    else:
        # Если файл не соответствует ожидаемому, возвращаем результат функции выбора
        return function_choice(file_path)

# Пример вывода первых элементов файла (можно раскомментировать для отладки)
# print(
#     "\nОбрабатывается operations.json"
#     + f"\nДля удобства выведу вам пару первых элементов:\n{function_choice(file_path)[:2]}"
# )