import unittest
import logging
from src.client.usa_stock_market.__tools import check_columns, ColType, RequestContext, WrongColumnsException, Column
from src.api.request_context import Filter, Sort


class CheckColumns_TestCase(unittest.TestCase):

    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    def test_WHEN_give_correct_columns_THEN_no_errors(self):
        # Array

        # Act
        check_columns(RequestContext(filters=[Filter("type", Filter.CompareFunc.eq, "eoue"), Filter("market_cap_basic", Filter.CompareFunc.eq, 2323)], sort=Sort("volume")), [
                      Column.el_name, Column.stocks, Column.market_cap], ColType.SECTOR)
        # Assert

    def test_WHEN_give_incorrect_columns_THEN_no_errors(self):
        # Array

        # Act

        # Assert
        with self.assertRaises(WrongColumnsException) as context:
            check_columns(RequestContext(filters=[Filter("type", Filter.CompareFunc.eq, "eoue"), Filter("market_cap_basic", Filter.CompareFunc.eq, 2323)], sort=Sort("volume")), [
                Column.el_name, Column.dividend_per_share, Column.market_cap], ColType.SECTOR)

        with self.assertRaises(WrongColumnsException) as context:
            check_columns(RequestContext(filters=[Filter("dps_common_stock_prim_issue_fy", Filter.CompareFunc.eq, "eoue"), Filter("market_cap_basic", Filter.CompareFunc.eq, 2323)], sort=Sort("volume")), [
                Column.el_name, Column.stocks, Column.market_cap], ColType.SECTOR)

        with self.assertRaises(WrongColumnsException) as context:
            check_columns(RequestContext(filters=[Filter("typesss", Filter.CompareFunc.eq, "eoue"), Filter("market_cap_basic", Filter.CompareFunc.eq, 2323)], sort=Sort("volume")), [
                Column.el_name, Column.stocks, Column.market_cap], ColType.SECTOR)

        with self.assertRaises(WrongColumnsException) as context:
            check_columns(RequestContext(filters=[Filter("type", Filter.CompareFunc.eq, "eoue"), Filter("market_cap_basic", Filter.CompareFunc.eq, 2323)], sort=Sort("dps_common_stock_prim_issue_fy")), [
                Column.el_name, Column.stocks, Column.market_cap], ColType.SECTOR)
        with self.assertRaises(WrongColumnsException) as context:
            check_columns(RequestContext(filters=[Filter("type", Filter.CompareFunc.eq, "eoue"), Filter("market_cap_basic", Filter.CompareFunc.eq, 2323)], sort=Sort("volumess")), [
                Column.el_name, Column.stocks, Column.market_cap], ColType.SECTOR)
