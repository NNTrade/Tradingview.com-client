import unittest
import logging
from src.parser.scan_json_parser import scan_json_parse
import json


class ParseScanJSON_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def __init__(self, methodName: str = "runTest") -> None:
        self.industries_columns = ["description",
                                   "market",
                                   "market_cap_basic",
                                   "type",
                                   "typespecs",
                                   "fundamental_currency_code",
                                   "dividends_yield",
                                   "change",
                                   "volume",
                                   "sector",
                                   "basic_elements"]

        file_path = "./test/parser/mocks/industry_scan_response.json"
        with open(file_path, 'r') as file:
            self.response_json = json.loads(file.read())

        super().__init__(methodName)

    def test_WHEN_parse_json_THEN_get_correct_value(self):
        # Array
        excepted_idx = "INDUSTRY_US:COMMERCIAL.SERVICES.ADVERTISING.MARKETING.SERVICES"

        # Act
        asserted_df = scan_json_parse(
            self.industries_columns, self.response_json)

        # Assert
        self.assertIsNotNone(asserted_df)

        self.assertEqual(asserted_df.index.name, "Id")
        self.assertEqual(len(asserted_df.index), 5)
        for expected_column in self.industries_columns:
            self.assertTrue(expected_column in asserted_df.columns,
                            f'Columns does not contain {expected_column}')

        self.assertTrue(excepted_idx in asserted_df.index,
                        f"{excepted_idx} does not find in index {asserted_df.index}")

        self.assertEqual(asserted_df["description"][excepted_idx],
                         "Advertising/Marketing Services")

        self.assertEqual(asserted_df["market"][excepted_idx],
                         "america")

        self.assertEqual(asserted_df["market_cap_basic"][excepted_idx],
                         53815523830.6627)

        self.assertEqual(asserted_df["type"][excepted_idx],
                         "industry")
        self.assertEqual(asserted_df["typespecs"][excepted_idx],
                         None)
        self.assertEqual(asserted_df["fundamental_currency_code"][excepted_idx],
                         "USD")
        self.assertEqual(asserted_df["dividends_yield"][excepted_idx],
                         2.89775035)
        self.assertEqual(asserted_df["change"][excepted_idx],
                         0.72529268)
        self.assertEqual(asserted_df["volume"][excepted_idx],
                         442959.7059306)
        self.assertEqual(asserted_df["sector"][excepted_idx],
                         "Commercial Services")
        self.assertEqual(asserted_df["basic_elements"][excepted_idx],
                         36)
