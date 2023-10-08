import unittest
import logging
from src.client.columns import ColumnInfo, ColumnType, Column


class Column_TestCase(unittest.TestCase):

  logger = logging.getLogger(__name__)
  logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                      datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

  def test_WHEN_isAllowedFor_THEN_get_correct_answer(self):
    # Array
    test_col = ColumnInfo(Column.volume, "test column", [
                          ColumnType.INDUSTRY, ColumnType.STOCK])
    # Act

    # Assert
    self.assertTrue(test_col.is_allowed_for(ColumnType.INDUSTRY))
    self.assertTrue(test_col.is_allowed_for(ColumnType.STOCK))
    self.assertFalse(test_col.is_allowed_for(ColumnType.SECTOR))

  def test_WHEN_equal_THEN_correct_response(self):
    # Array
    test1_col = ColumnInfo(Column.volume, "test column", [
        ColumnType.INDUSTRY, ColumnType.STOCK])
    test2_col = ColumnInfo(Column.volume, "test column", [
        ColumnType.INDUSTRY, ColumnType.STOCK])
    test3_col = ColumnInfo(Column.volume, "test column", [
        ColumnType.INDUSTRY, ColumnType.SECTOR])
    # Act

    # Assert
    self.assertTrue(test1_col == test2_col)
    self.assertFalse(test1_col == test3_col)
