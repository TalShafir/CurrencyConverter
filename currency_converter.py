import argparse
import sys

from input_file_parser import InputFileParser
from currency_converter_service import CurrencyConverterServiceFactory

_INPUT_FILE_HELP = "file that contains source and target currencies and a list of values, all separated by nextline"


def parse_args(argv):
    """
    Parses the arguments given in argv using argparse which also provides automatic --help
    :param argv: the argv (excluding argv[0])
    :return: Namespace object containing the parsed argv
    """
    parser = argparse.ArgumentParser(description="Tool to convert currency")

    parser.add_argument("-f", "--input-file", type=str, help=_INPUT_FILE_HELP)

    return parser.parse_args(argv)


def currency_converter(input_file, input_file_parser_service=None, converter_service=None):
    src_currency, target_currency, values = input_file_parser_service.parse(input_file)
    converted_values = [converter_service.convert(src_currency, target_currency, value) for value in values]
    return converted_values


def main(argv):
    args = parse_args(argv)
    input_file_parser = InputFileParser()
    converter_service = CurrencyConverterServiceFactory.from_config_file('currency_converter.config')

    print('\n'.join(currency_converter(input_file=args.input_file,
                                       input_file_parser_service=input_file_parser,
                                       converter_service=converter_service)))


if __name__ == '__main__':
    main(argv=sys.argv[1:])
