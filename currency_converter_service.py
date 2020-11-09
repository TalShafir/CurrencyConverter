from configparser import ConfigParser
import os

import requests


class CurrencyConverterService:
    """
    Service that handles the requests to the currency converter API
    """

    def __init__(self, api_key, api_endpoint_address):
        """

        :param api_key: api_key given by the service provider
        :param api_endpoint_address: address of the API endpoint
        """
        self.api_key = api_key
        self.api_endpoint_address = api_endpoint_address

    def convert(self, source_currency: str, target_currency: str, value: float) -> float:
        """
        Converts the value in source_currency to its appropriate value in target_currency
        :param source_currency: str representing the source currency (i.e USD)
        :param target_currency: str representing the target currency (i.e USD)
        :param value: the value in source currency
        :return: the converted value in the target currency
        """
        currencies = self._currency_format(source_currency, target_currency)
        req = requests.get(self.api_endpoint_address, params={
            'apiKey': self.api_key,
            'compact': 'ultra',
            'q': currencies
        })

        if req.status_code != 200:
            # TODO
            raise Exception('Failed')

        return value * req.json()[currencies]

    @staticmethod
    def _currency_format(source_currency: str, target_currency: str) -> str:
        """
        format the currencies to the required format the service provider requires
        :param source_currency: str representing the source currency (i.e USD)
        :param target_currency: str representing the target currency (i.e USD)
        :return: the conversion string
        """
        return source_currency.upper() + '_' + target_currency.upper()


class CurrencyConverterServiceFactory:
    @staticmethod
    def from_config_file(file_path: str) -> CurrencyConverterService:
        config = ConfigParser()
        config.read(file_path)
        # validate config
        if 'AUTH' not in config.sections():
            raise Exception("The config file doesn't contain 'AUTH' section")

        if not ('api_key' in config['AUTH'] and 'api_endpoint_address' in config['AUTH']):
            raise Exception("The config file doesn't contain 'api_key' or 'api_endpoint_address' in 'AUTH' section")

        converter_service = CurrencyConverterService(api_key=config['AUTH']['api_key'],
                                                     api_endpoint_address=config['AUTH']['api_endpoint_address'])
        return converter_service
