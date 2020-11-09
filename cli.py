import argparse
import sys

from input_file_parser import InputFileParser


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


def main(argv=None, input_file_parser=None):
    args = parse_args(argv)
    src_currency, target_currency, values = input_file_parser.parse(args.input_file)
    for value in values:
        print(convert(src_currency, target_currency, value))


def convert(src_currency: str, target_currency: str, value: str) -> float:
    """
    Converts the value in src_currency to its converted value as target_currency
    :param src_currency: str representing the src_currency
    :param target_currency: str representing the target_currency
    :param value: the value to be converted as str
    :return: the converted value as float
    """
    raise NotImplementedError()


if __name__ == '__main__':
    input_file_parser = InputFileParser()
    main(argv=sys.argv[1:], input_file_parser=input_file_parser)
