import requests


class CurrencyConverterService:
    """
    Service that handles the requests to the currency converter API
    """
    def __init__(self, api_key, api_endpoint_address):
        self.api_key = api_key
        self.api_endpoint_address = api_endpoint_address

    def convert(self, source_currency: str, target_currency: str, value: float) -> float:
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
        return source_currency.upper() + '_' + target_currency.upper()
