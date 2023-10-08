import unittest
import logging
from src.parser.sector_parser import sectors_response_parse
from src.parser._parse_tools import parse_header_from_payload


class ParseHeader_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def __init__(self, methodName: str = "runTest") -> None:
        file_path = "./test/parser/mocks/sector_request_response.html"
        with open(file_path, 'r') as file:
            self.test_response = file.read()
        self.expected_headers = ["Sector", "Market cap", "Dividend yield FWD %",
                                 "Change % 1D", "Volume 1D", "Industries", "Stocks"]

        super().__init__(methodName)

    def test_WHEN_request_header_THEN_get_correct_header(self):
        # Array
        # Act
        asserted_header = parse_header_from_payload(self.test_response)

        # Assert
        for expected_header in self.expected_headers:
            self.assertTrue(expected_header in asserted_header)


class SectorParse_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def __init__(self, methodName: str = "runTest") -> None:
        file_path = "./test/parser/mocks/sector_request_response.html"
        with open(file_path, 'r') as file:
            self.test_response = file.read()

        super().__init__(methodName)

    def test_WHEN_parse_response_THEN_get_correct_data(self):
        # Array
        expected_columns = ["Market cap", "Market cap currency", "Dividend yield FWD rel",
                            "Change rel 1D", "Volume 1D", "Industries", "Stocks", "Sector stocks URL"]
        # Act
        asserted_df = sectors_response_parse(self.test_response)

        # Assert
        self.assertEqual(asserted_df.index.name, "Sector")
        for expected_column in expected_columns:
            self.assertTrue(expected_column in asserted_df.columns,
                            f'Columns does not contain {expected_column}')

        self.assertTrue("Commercial Services" in asserted_df.index,
                        f"Commercial Services does not find in index {asserted_df.index}")

        self.assertEqual(asserted_df["Market cap"]["Commercial Services"],
                         1.639*pow(10, 12))
        self.assertEqual(asserted_df["Market cap currency"]
                         ["Commercial Services"], "USD")
        self.assertEqual(asserted_df["Dividend yield FWD rel"]["Commercial Services"],
                         0.0079)
        self.assertEqual(asserted_df["Change rel 1D"]["Commercial Services"],
                         -0.0027)
        self.assertEqual(asserted_df["Volume 1D"]["Commercial Services"],
                         1.117*pow(10, 6))
        self.assertEqual(asserted_df["Industries"]["Commercial Services"],
                         5)
        self.assertEqual(asserted_df["Stocks"]["Commercial Services"],
                         252)
        self.assertEqual(asserted_df["Sector stocks URL"]["Commercial Services"],
                         '/markets/stocks-usa/sectorandindustry-sector/commercial-services/')

        self.assertEqual(asserted_df["Market cap"]["Industrial Services"],
                         880.605*pow(10, 9))
