from typing import Tuple, List


class InputFileParser:
    @staticmethod
    def parse(file_path: str) -> Tuple[str, str, List[str]]:
        with open(file_path, 'r') as input_file:
            # load currencies
            src_currency, target_currency = next(input_file), next(input_file)
            values = list(input_file)
            return src_currency, target_currency, values
