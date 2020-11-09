# CurrencyExchanger

![Python application](https://github.com/TalShafir/CurrencyConverter/workflows/Python%20application/badge.svg)

A simple tool to convert currencies powered by [CurrencyConverterAPI](https://www.currencyconverterapi.com/)

Config
-----
Need to edit the `currency_converter.config` and add a generated `API_KEY` from [CurrencyConverterAPI](https://www.currencyconverterapi.com/).


Usage
-----
```sh
python -m pip install -r requirements.txt
python currency_converter.py -f /path/to/file
```

The file should be in the following format:
```text
SRC_CURRENCY
TARGET_CURRENCY
value-1
...
value-N
```

For example:
```text
USD
EUR
12
50
120
400
```
