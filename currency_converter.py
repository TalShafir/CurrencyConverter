import argparse
import sys
from configparser import ConfigParser

from input_file_parser import InputFileParser
from currency_converter_service import CurrencyConverterService


def parse_args(argv):
    """
    Parses the arguments given in argv using argparse which also provides automatic --help
    :param argv: the argv (excluding argv[0])
    :return: Namespace object containing the parsed argv
    """
    parser = argparse.ArgumentParser(description="Tool to convert currency")
    parser.add_argument("-f", "--input-file", type=str,
                        help="input file that contains source currency, target currency and a list of values, all seperated by nextline")

    return parser.parse_args(argv)


def main(argv=None, input_file_parser_service=None, converter_service=None):
    args = parse_args(argv)
    src_currency, target_currency, values = input_file_parser_service.parse(args.input_file)
    for value in values:
        print(converter_service.convert(src_currency, target_currency, value))


if __name__ == '__main__':
    input_file_parser = InputFileParser()

    config = ConfigParser()
    config.read('currency_converter.config')
    converter_service = CurrencyConverterService(api_key=config['AUTH']['api_key'],
                                                 api_endpoint_address=config['AUTH']['api_endpoint_address'])

    main(argv=sys.argv[1:], input_file_parser_service=input_file_parser, converter_service=converter_service)