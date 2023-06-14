import unittest
import logging
from src.parser.industry_parser import industry_response_parse
import json


class IndustryParser_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def __init__(self, methodName: str = "runTest") -> None:
        file_path = "./test/parser/mocks/industry_request_response.html"
        with open(file_path, 'r') as file:
            self.test_response = file.read()

        super().__init__(methodName)

    def test_WHEN_parse_THEN_get_correct_data(self):
        # Array
        expected_columns = ["Market cap", "Market cap currency", "Dividend yield FWD rel",
                            "Change rel 1D", "Volume 1D", "Stocks", "Sector", "Sector URL", "Industry URL"]
        # Act
        asserted_df = industry_response_parse(self.test_response)

        # Assert
        self.assertEqual(asserted_df.index.name, "Industry")
        for expected_column in expected_columns:
            self.assertTrue(expected_column in asserted_df.columns,
                            f'Columns does not contain {expected_column}')

        self.assertTrue("Advertising/Marketing Services" in asserted_df.index,
                        f"Advertising/Marketing Services does not find in index {asserted_df.index}")

        self.assertEqual(asserted_df["Market cap"]["Advertising/Marketing Services"],
                         53.481*pow(10, 9))
        self.assertEqual(asserted_df["Market cap currency"]
                         ["Advertising/Marketing Services"], "USD")

        self.assertEqual(asserted_df["Dividend yield FWD rel"]["Advertising/Marketing Services"],
                         0.0292)
        self.assertAlmostEqual(asserted_df["Change rel 1D"]["Advertising/Marketing Services"],
                               0.0071)

        self.assertEqual(asserted_df["Volume 1D"]["Advertising/Marketing Services"],
                         1.807*pow(10, 6))

        self.assertEqual(asserted_df["Sector"]["Advertising/Marketing Services"],
                         "Commercial Services")
        self.assertEqual(asserted_df["Sector URL"]["Advertising/Marketing Services"],
                         '/markets/stocks-usa/sectorandindustry-sector/commercial-services/')

        self.assertEqual(asserted_df["Stocks"]["Advertising/Marketing Services"],
                         36)

        self.assertEqual(asserted_df["Industry URL"]["Advertising/Marketing Services"],
                         '/markets/stocks-usa/sectorandindustry-industry/advertising-marketing-services/')


