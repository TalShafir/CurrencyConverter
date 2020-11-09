import argparse
import sys


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


def main(argv=None):
    args = parse_args(argv)
    with open(args.input_file, 'r') as input_file:
        # load currencies
        src_currency, target_currency = next(input_file), next(input_file)

        # run for all the values
        for value in input_file:
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


class InputFileParser:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(self.file_path, 'r') as input_file:
            # load currencies
            self.src_currency, self.target_currency = next(input_file), next(input_file)
            self.values = list(input_file)



if __name__ == '__main__':
    main(sys.argv[1:])
