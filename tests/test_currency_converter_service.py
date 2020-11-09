import unittest

from currency_converter_service import CurrencyConverterServiceFactory


class TestCurrencyConverterService(unittest.TestCase):
    service = CurrencyConverterServiceFactory.from_config_file('currency_converter.config')

    def test_sanity(self):
        self.assertEqual(self.service.convert('USD', 'USD', 1), 1)

    def test_service(self):
        conversion_ratio = self.service.convert('USD', 'ILS', 1)
        value = 50
        self.assertEqual(value * conversion_ratio, self.service.convert('USD', 'ILS', value))


if __name__ == '__main__':
    unittest.main()
