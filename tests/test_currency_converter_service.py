import unittest

from currency_converter_service import CurrencyConverterServiceFactory


class TestCurrencyConverterService(unittest.TestCase):
    """
    Tests to make sure that the we can access the service provider
    """
    service = CurrencyConverterServiceFactory.from_config_file('currency_converter.config')

    def test_sanity(self):
        """
        try to get the conversion rate from USD to USD which must be equal to 1
        """
        self.assertEqual(self.service.convert('USD', 'USD', 1), 1)

    def test_service(self):
        """
        test that our service calculate the converted value correctly given the ratio from the provider
        """
        conversion_ratio = self.service.convert('USD', 'ILS', 1)
        value = 50
        self.assertEqual(value * conversion_ratio, self.service.convert('USD', 'ILS', value))


if __name__ == '__main__':
    unittest.main()
