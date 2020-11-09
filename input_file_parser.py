from collections import namedtuple

ParsedInput = namedtuple('ParsedInput', ['src_currency', 'target_currency', 'values'])


class InputFileParser:
    """
    Simple wrapper class for the parse function
    """

    @staticmethod
    def parse(file_path: str) -> ParsedInput:
        """
        Parses input file according the given format:
            source_currency
            target_currency
            value-1
            ...
            value-n

        with the values and currencies each separated by a newline

        :param file_path: a path to a file in the given format
        :return: named tuple containing the currencies and list of values
        """
        with open(file_path, 'r') as input_file:
            # load currencies
            src_currency, target_currency = next(input_file), next(input_file)
            # load values
            values = list(map(float, filter(lambda val: val, input_file)))
            return ParsedInput(src_currency=src_currency.strip().upper(),
                               target_currency=target_currency.strip().upper(),
                               values=values)
