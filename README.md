# Генератор транзакций

## Новые функции

### 1. `filter_by_currency(transactions, currency)`
- Генератор, который фильтрует транзакции по заданной валюте.
- **Параметры:**
  - `transactions`: Список транзакций (каждая транзакция представлена словарем).
  - `currency`: Код валюты для фильтрации.
  
### 2. `transaction_descriptions(transactions)`
- Генератор, который возвращает описания транзакций.
- **Параметры:**
  - `transactions`: Список транзакций.

### 3. `card_number_generator(start, end)`
- Генератор, который возвращает номера карт в формате "XXXX XXXX XXXX XXXX".
- **Параметры:**
  - `start`: Начальное число (0 - 9999).
  - `end`: Конечное число (0 - 9999).

## Пример использования
```python
from generators import filter_by_currency, transaction_descriptions, card_number_generator

# Пример использования filter_by_currency
transactions = [...]  # Ваш список транзакций
for transaction in filter_by_currency(transactions, "USD"):
    print(transaction)

# Пример использования transaction_descriptions
for description in transaction_descriptions(transactions):
    print(description)

# Пример использования card_number_generator
for card_number in card_number_generator(0, 5):
    print(card_number)
