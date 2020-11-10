import argparse
import sys
from typing import List

from dependency_injector import containers, providers
from dependency_injector.wiring import Provide

from input_file_parser import InputFileParser
from currency_converter_service import CurrencyConverterService

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


class Container(containers.DeclarativeContainer):
    """
    Container class to manage the dependency injection
    """
    config = providers.Configuration()

    input_file_parser = providers.Singleton(
        InputFileParser
    )

    converter_service = providers.Singleton(
        CurrencyConverterService,
        api_key=config.AUTH.api_key,
        api_endpoint_address=config.AUTH.api_endpoint_address,
    )


def currency_converter(input_file: str,
                       input_file_parser_service: InputFileParser = Provide[Container.input_file_parser],
                       converter_service: CurrencyConverterService = Provide[Container.converter_service]) \
        -> List[float]:
    src_currency, target_currency, values = input_file_parser_service.parse(input_file)
    converted_values = [converter_service.convert(src_currency, target_currency, value) for value in values]
    return converted_values


def main(argv):
    # read argv
    args = parse_args(argv)

    # configure dependency injection
    container = Container()
    container.config.from_ini('currency_converter.config')
    container.wire(modules=[sys.modules[__name__]])

    # execute the conversion
    converted_values = currency_converter(args.input_file)
    # join the values to be one string separated by \n
    print('\n'.join(
        # for each value round it 2 digits after the decimal point and convert to string
        map(lambda val: str(round(val, 2)),
            converted_values)))


if __name__ == '__main__':
    main(argv=sys.argv[1:])
