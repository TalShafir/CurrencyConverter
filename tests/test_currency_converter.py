import unittest
from unittest.mock import patch, mock_open

from currency_converter_service import CurrencyConverterService
from input_file_parser import InputFileParser
from currency_converter import currency_converter


class TestCurrencyConverter(unittest.TestCase):
    def test_currency_converter(self):
        _TEST_INPUT_FILE = """USD
                               ILS
                               1
                               5
                               10.5"""
        with patch("builtins.open", mock_open(read_data=_TEST_INPUT_FILE)):
            converted_values = currency_converter('/path/to/input',
                                                  input_file_parser_service=InputFileParser(),
                                                  converter_service=MockCurrencyConverterService(None, None))
            self.assertEqual(converted_values, [3.5, 17.5, 36.75])

    def test_no_values(self):
        _TEST_INPUT_FILE = """USD
                               ILS"""
        with patch("builtins.open", mock_open(read_data=_TEST_INPUT_FILE)):
            converted_values = currency_converter('/path/to/input',
                                                  input_file_parser_service=InputFileParser(),
                                                  converter_service=MockCurrencyConverterService(None, None))
            self.assertEqual(converted_values, [])


class MockCurrencyConverterService(CurrencyConverterService):
    def convert(self, source_currency: str, target_currency: str, value: float) -> float:
        _MOCK_CURRENCIES = {
            ('USD', 'ILS'): 3.5,
            ('USD', 'USD'): 1.0,
            ('ILS', 'ILS'): 1.0,
        }
        return value * _MOCK_CURRENCIES[(source_currency, target_currency)]


if __name__ == '__main__':
    unittest.main()
