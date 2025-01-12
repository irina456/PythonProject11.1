# Генераторы для работы с транзакциями

## Описание

Модуль `generators` предоставляет инструменты для фильтрации и извлечения информации из больших массивов данных транзакций.

## Установленные функции

### `filter_by_currency(transactions, currency)`

Генератор, который фильтрует транзакции по заданной валюте.

**Пример использования:**
```python
usd_transactions = filter_by_currency(transactions, "USD")
for transaction in usd_transactions:
    print(transaction)
