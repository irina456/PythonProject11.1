# Генераторы для работы с транзакциями

## Описание

Модуль `generators` предоставляет инструменты для фильтрации и извлечения информации из больших массивов данных транзакций.

## Установленные функции

### `filter_by_currency(transactions, currency)`

Генератор, который фильтрует транзакции по заданной валюте.

## Тестирование

Проект включает юнит-тесты pytest.

*Текущие результаты тестирования:*

Для запуска тестов выполните команду:
- при активированном виртуальном окружении:
```
pytest --cov
 
```
- через poetry:
```
poetry run pytest --cov
```

```
============================== test session starts ===========================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\Oper\PycharmProjects\pythonProject\bank_widget
configfile: pyproject.toml
plugins: cov-6.0.0
collected 82 items                                                                                                                   

tests\test_decorators.py ....                            [  4%]
tests\test_external_api.py ..........                    [ 17%]
tests\test_generators.py ..............                  [ 34%]
tests\test_masks.py ..............                       [ 51%]
tests\test_processing.py ........                        [ 60%]
tests\test_read_transactions.py ......                   [ 68%]
tests\test_utils.py .........                            [ 79%]
tests\test_widget.py .................                   [100%]

---------- coverage: platform win32, python 3.13.1-final-0 -----------
Name                              Stmts   Miss  Cover
-----------------------------------------------------
decorators.py                        37      4    89%
src\__init__.py                       0      0   100%
src\external_api.py                  45      5    89%
src\generators.py                    38      2    95%
src\masks.py                         57      1    98%
src\processing.py                    23      0   100%
src\read_transactions.py             18      2    89%
src\utils.py                         44      0   100%
src\widget.py                        33      1    97%
tests\__init__.py                     0      0   100%
tests\conftest.py                    68      3    96%
tests\test_decorators.py             15      0   100%
tests\test_external_api.py           55      0   100%
tests\test_generators.py             54      0   100%
tests\test_masks.py                  25      0   100%
tests\test_processing.py             16      0   100%
tests\test_read_transactions.py      34      0   100%
tests\test_utils.py                  46      0   100%
tests\test_widget.py                 23      2    91%
-----------------------------------------------------
TOTAL                               631     20    97%


======================================================== 82 passed in 1.24s ===

- в папке `htmlcov\` проекта содержится файл `index.html` с отчетом о покрытии тестами
- в рамках тестирования проекта использованы фикстуры, параметризация тестов,
а также тестирование исключений с помощью `pytest.raises`.


## Примеры работы функций:

1. Пример маскировки номера для карты:

```Visa Platinum 7000792289606361```  - входной аргумент
```Visa Platinum 7000 79** **** 6361```  - выход функции

2. Пример маскировки номера для счета:

```Счет 73654108430135874305```  - входной аргумент
```Счет **4305```  - выход функции

3. Пример преобразования формата даты:

```2024-03-11T02:26:18.671407```  - входной аргумент
```11.03.2024```  - выход функции

4. Пример работы функции фильтра операций:

входные данные с аргументом 'EXECUTED':
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
выход функции, если вторым аргументом передано 'CANCELED':
```
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
5. Пример работы функции сортировки по дате:

входные данные:
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
выход функции (сортировка по убыванию, т. е. сначала самые последние операции):
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
6. Пример работы функции, фильтрующий операции по заданной валюте:

входные данные:
```
[
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
```

выход функции при заданной валюте 'USD':

```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
       ```

7. Пример работы функции, возвращающей описание операций:

*входные данные (см. предыдущий пример)*

*выходные данные:*
```
Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
```

8. Пример работы функции - генератора номеров карт:

входные данные(первый и последний номера карт, которые необходимо сгенерировать, - 1, 5)

выход функции:
```
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
```

9. Пример работы декоратора `log`:

пример использования декоратора:

```
@log(filename="mylog.txt")
def my_function(x, y):
"""
    Выполняет деление полученных значений
    :param x:
    :param y:
    :return:
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if not ((type(x) is int or type(x) is float) and (type(y) is int or type(x) is float)):
        raise TypeError("Value must be an integer or float")
    return x / y

print(my_function(1, 2))

```
вывод в лог-файл `mylog.txt` при успешном выполнении:

```
my_function with args: (1, 2) and kwargs: {}. 
Result = 0.5.
Function call time: 2025-01-05 18:04:07.298253.
Time execution: 0.0000019
```
10. Пример работы main():
Входные данные:
`path_to_file = path()`
`data_transactions = get_read_file(path_to_file)`
`random_number = get_random_number(data_transactions)`
`result_transactions = get_conversion_apilayer(random_number, data_transactions)` 

Выходные дынные:
'''Сумма транзакции составляет 62654.3 USD или 6422003.28 рублей в соответствии с текущим 
курсом валют на дату: 2025-01-17.'''

11. Пример работы main_rub():
Входные данные:
`transactions_rub = data_for_test_rub()`
`random_number = get_random_number(transactions_rub)`
`result_transactions = get_conversion_apilayer(random_number, transactions_rub)`

Выходные данные:
'''Сумма транзакции составляет 55149.24 RUB.'''

12. Пример работы get_read_csv():
Входные данные - файл `transactions.csv`

Выходные данные:
```
 {
        "id":650703.0,
        "state":"EXECUTED",
        "date":"2023-09-05T11:30:32Z",
        "amount":16210.0,
        "currency_name":"Sol",
        "currency_code":"PEN",
        "from":"Счет 58803664561298323391",
        "to":"Счет 39745660563456619397",
        "description":"Перевод организации"
    }
...
```

13. Пример работы get_read_excel():
Входные данные - файл `transactions_excel.xlsx`

Выходные данные:
```
{'id': 650703.0, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210.0, 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}
...
```
