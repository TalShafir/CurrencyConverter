import unittest
from unittest.mock import patch, mock_open

from input_file_parser import InputFileParser


class InputFileParserTest(unittest.TestCase):
    """
    Test cases for input parsing
    """

    def test_file_parsing(self):
        """
        Test with a normal case that the parsing works
        """
        _TEST_INPUT_FILE = """USD
                            ILS
                            1
                            5
                            10.5"""
        with patch("builtins.open", mock_open(read_data=_TEST_INPUT_FILE)):
            input_file_parser = InputFileParser()
            parsed_input = input_file_parser.parse("path/to/open")
            self.assertEqual(parsed_input.src_currency, "USD")
            self.assertEqual(parsed_input.target_currency, "ILS")
            self.assertEqual(parsed_input.values, [1.0, 5.0, 10.5])

    def test_no_val_file_parsing(self):
        """
        Test in case of no values to convert that the parsing works correctly
        """
        _TEST_INPUT_FILE = """USD
                            ILS"""
        with patch("builtins.open", mock_open(read_data=_TEST_INPUT_FILE)):
            input_file_parser = InputFileParser()
            parsed_input = input_file_parser.parse("path/to/open")
            self.assertEqual(parsed_input.src_currency, "USD")
            self.assertEqual(parsed_input.target_currency, "ILS")
            self.assertEqual(parsed_input.values, [])


if __name__ == '__main__':
    unittest.main()
