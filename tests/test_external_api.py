from unittest.mock import patch

import pytest

from src.external_api import conversion_from_usd_eur_in_rub


@patch("requests.get")
def test_conversion_from_usd_eur_in_rub(mock_api, return_api):
    mock_api.return_value.json.return_value = return_api
    assert str(type(conversion_from_usd_eur_in_rub(100, "EUR"))) == "<class 'float'>"
    mock_api.assert_called()


# The expected result is negative
@pytest.mark.parametrize(
    "sum, key, expected",
    [
        (10, None, '''Укажите валюту в нужном формате "USD" или "EUR"'''),
        (10, 121321424, '''Укажите валюту в нужном формате "USD" или "EUR"'''),
        (10, [], '''Укажите валюту в нужном формате "USD" или "EUR"'''),
    ],
)
def test_conversion_from_usd_eur_in_rub_valueError(sum, key, expected):
    with pytest.raises(ValueError):
        assert conversion_from_usd_eur_in_rub(sum, key) == expected


@patch("requests.get")
def test_conversion_from_usd_eur_in_rub_invalid_data(mock_api, return_api_error):
    mock_api.return_value.json.return_value = return_api_error
    with pytest.raises(ValueError):
        assert conversion_from_usd_eur_in_rub("___", "EUR") == "Error, invalid data or not correct url"
    mock_api.assert_called()
