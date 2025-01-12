from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":
    operations = [
        {'id': 41428829, 'state': 'EXECUTED',
         'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED',
         'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED',
         'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED',
         'date': '2018-10-14T08:21:33.419441'}
    ]

    # Примеры для тестирования функции filter_by_state
    print(filter_by_state(operations))  # Выход функции
    # со статусом по умолчанию 'EXECUTED'
    print(filter_by_state(operations, 'CANCELED'))  # Выход функции,
    # если вторым аргументом передано 'CANCELED'

    # Примеры для тестирования функции sort_by_date
    print(sort_by_date(operations))  # Выход функции (сортировка по убыванию)