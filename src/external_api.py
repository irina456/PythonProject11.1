import os

import requests
from dotenv import load_dotenv


def conversion_from_usd_eur_in_rub(
    transaction_sum: int = 0,
    currency: str = "",
    url: str = "https://api.apilayer.com/exchangerates_data/convert",
    filename: str = "log/ex_api.log",
) -> float:
    """Принимает на вход сумму в валюте и наименование валюты "RUB" или "USD"
    Возвращает число типа "float" - валюта, конвертированная в рубли
    Также имеет 1 доп параметр:
    - url ссылка на апи"""

    if currency == "USD" or currency == "EUR":
        payload = {"to": "RUB", "from": currency, "amount": str(transaction_sum)}

        try:
            load_dotenv()
            api_key = os.getenv("API_KEY")
            headers = {"apikey": api_key}
            temp = requests.get(url, headers=headers, params=payload)
            with open(filename, "a") as file:
                file.write(f"OUTPUT DATA:\n{temp.json()["result"]}\n")
            return float(temp.json()["result"])

        except Exception:
            with open(filename, "a") as file:
                file.write(f"ERROR:\n{temp.json()}\n")
            raise ValueError("Error, invalid data or not correct url")
    else:
        raise ValueError('''Укажите валюту в нужном формате "USD" или "EUR"''')
