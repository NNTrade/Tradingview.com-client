import unittest
import logging
from src.exceptions import UnparsableNumber
from src.parser.number_parser import parse_number, convert_percent_to_mult
import numpy as np


class NumberParser_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_give_string_THEN_get_answer(self):
        # Array
        # Thousand	3	1 (1, 000)
        # Ten thousand	4	(10, 000)
        # Hundred thousand	5	(100, 000)
        # Million	6	2 (1, 000, 000)
        # Billion	9	3 (1, 000, 000, 000)
        # Trillion	12	4 (1, 000, 000, 000, 000)
        # Act

        # Assert
        self.assertEqual(0.12, parse_number("12%"))
        self.assertEqual(0.0102, parse_number("1.02%"))
        self.assertEqual(0.0002, parse_number("0.02%"))

        self.assertEqual(12, parse_number("12"))
        self.assertEqual(1.02, parse_number("1.02"))
        self.assertEqual(0.02, parse_number("0.02"))

        self.assertEqual(12000, parse_number("12K"))
        self.assertEqual(1020, parse_number("1.02K"))
        self.assertEqual(20, parse_number("0.02K"))

        self.assertEqual(12*pow(10, 6), parse_number("12M"))
        self.assertEqual(1.02*pow(10, 6), parse_number("1.02M"))
        self.assertEqual(0.02*pow(10, 6), parse_number("0.02M"))

        self.assertEqual(12*pow(10, 9), parse_number("12B"))
        self.assertEqual(1.02*pow(10, 9), parse_number("1.02B"))
        self.assertEqual(0.02*pow(10, 9), parse_number("0.02B"))

        self.assertEqual(12*pow(10, 12), parse_number("12T"))
        self.assertEqual(1.02*pow(10, 12), parse_number("1.02T"))
        self.assertEqual(0.02*pow(10, 12), parse_number("0.02T"))

        self.assertEqual(12*pow(10, 15), parse_number("12Q"))
        self.assertEqual(1.02*pow(10, 15), parse_number("1.02Q"))
        self.assertEqual(0.02*pow(10, 15), parse_number("0.02Q"))

    def test_WHEN_get_unexpected_word_THEN_exception(self):
        # Array

        # Act

        # Assert
        with self.assertRaises(UnparsableNumber) as context:
            parse_number("12W")

    def test_WHEN_number_has_long_minus_simbol_THEN_(self):
        # Array
        # some times used − instead of -, it is different simbols but looking like the same

        value = '−0.05%'

        # Act

        # Assert
        self.assertEqual(-0.0005, parse_number(value))

    def test_WHEN_minus_THEN_Nan(self):
        # Array

        # Act

        # Assert
        self.assertIsNone(parse_number(None))
        self.assertIsNone(parse_number("−"))
        self.assertIsNone(parse_number("—"))
        self.assertIsNone(parse_number("-"))


class ConvertPercentToMultconvert_percent_to_mult_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_give_value_THEN_convert_correctly(self):
    # Array

    # Act

    # Assert
    self.assertEqual(0.01, convert_percent_to_mult(1))
    self.assertEqual(-0.01, convert_percent_to_mult(-1))

    self.assertEqual(1, convert_percent_to_mult(100))
    self.assertEqual(-1, convert_percent_to_mult(-100))

    self.assertEqual(0.001, convert_percent_to_mult(0.1))
    self.assertEqual(-0.001, convert_percent_to_mult(-0.1))

    self.assertEqual(0, convert_percent_to_mult(0))

  def test_WHEN_give_None_or_minus_THEN_return_none(self):
    # Array

    # Act

    # Assert
    self.assertIsNone(convert_percent_to_mult(None))
    self.assertIsNone(convert_percent_to_mult("−"))
    self.assertIsNone(convert_percent_to_mult("—"))
    self.assertIsNone(convert_percent_to_mult("-"))
