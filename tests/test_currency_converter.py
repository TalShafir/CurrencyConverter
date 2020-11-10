import unittest
from unittest.mock import patch, mock_open
import sys

from currency_converter_service import CurrencyConverterService
from input_file_parser import InputFileParser
from currency_converter import currency_converter, Container


class TestCurrencyConverter(unittest.TestCase):
    """
    Tests for the whole conversion process
    """
    # configure dependency injection
    container = Container()
    container.wire(modules=[sys.modules[__name__]])

    def test_currency_converter(self):
        """
        Test the conversion process with a 'normal' case
        """
        _TEST_INPUT_FILE = """USD
                               ILS
                               1
                               5
                               10.5"""

        # mock the input file to be read from string
        with patch("builtins.open", mock_open(read_data=_TEST_INPUT_FILE)):
            # inject mock converter service
            with self.container.converter_service.override(MockCurrencyConverterService(None, None)):
                converted_values = currency_converter('/path/to/input')
                self.assertEqual(converted_values, [3.5, 17.5, 36.75])

    def test_no_values(self):
        """
        Test the conversion process with no values to convert
        """
        _TEST_INPUT_FILE = """USD
                               ILS"""
        # mock the input file to be read from string
        with patch("builtins.open", mock_open(read_data=_TEST_INPUT_FILE)):
            # inject mock converter service
            with self.container.converter_service.override(MockCurrencyConverterService(None, None)):
                converted_values = currency_converter('/path/to/input')
                self.assertEqual(converted_values, [])


class MockCurrencyConverterService(CurrencyConverterService):
    """
    A class that mocks for CurrencyConverterService
    """

    def convert(self, source_currency: str, target_currency: str, value: float) -> float:
        _MOCK_CURRENCIES = {
            ('USD', 'ILS'): 3.5,
            ('USD', 'USD'): 1.0,
            ('ILS', 'ILS'): 1.0,
        }
        return value * _MOCK_CURRENCIES[(source_currency, target_currency)]


if __name__ == '__main__':
    unittest.main()
