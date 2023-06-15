from __future__ import annotations
from ....api.symbol_query_types import SymbolQueryTypes
from typing import List, Dict
from enum import Enum
import pandas as pd


class ColType(Enum):
  INDUSTRY = "industry"
  SECTOR = "sector"
  STOCK = "stock"

  def toSymbolQueryTypes(self) -> SymbolQueryTypes:
    if self != ColType.STOCK:
      return SymbolQueryTypes(self.value)
    return None

class Column:
  def __init__(self, tech_name: str, description: str, allowedFor: List[ColType], rename: str = None, needPercentConvert: bool = False) -> None:
    if len(allowedFor) == 0:
      raise Exception("Column must be allowed at least for one client")
    self.__allowedFor = allowedFor
    self.__descripion = description
    self.__tech_name = tech_name
    self.__rename = rename if rename is not None else tech_name.capitalize()
    self.__needPercentConvert = needPercentConvert
    super().__init__()

  def is_allowed_for(self, colType: ColType) -> bool:
    return colType in self.__allowedFor

  @property
  def allowedFor(self) -> List[ColType]:
    return self.__allowedFor.copy()

  @property
  def description(self) -> str:
    return self.__descripion

  @property
  def tech_name(self) -> str:
    return self.__tech_name

  @property
  def name(self) -> str:
    return self.__rename

  @property
  def needPercentConvert(self) -> str:
    return self.__needPercentConvert

  def __eq__(self, __value: object) -> bool:
    if not isinstance(__value, Column):
      return False

    return self.name == __value.name and \
        self.tech_name == __value.tech_name and \
        self.needPercentConvert == __value.needPercentConvert and \
        len(self.__allowedFor) == len(
            __value.__allowedFor) and self.__allowedFor == __value.__allowedFor

  TECH_NAME_DICT_KEY = "Tech name"
  DESCRIPTION_DICT_KEY = "Description"
  NAME_DICT_KEY = "Name"
  NEED_PERCENT_CONVERT_DICT_KEY = "Need percent convert"
  ALLOWED_FOR = "Allowed for"
  ALLOWED_FOR_ENUM = "Allowed for enum"

  def to_dict(self) -> Dict[str, any]:
    return {Column.NAME_DICT_KEY: self.name,
            Column.DESCRIPTION_DICT_KEY: self.description,
            Column.TECH_NAME_DICT_KEY: self.tech_name,
            Column.NEED_PERCENT_CONVERT_DICT_KEY: self.needPercentConvert,
            Column.ALLOWED_FOR: [e.value for e in self.allowedFor],
            Column.ALLOWED_FOR_ENUM: self.allowedFor}

  @staticmethod
  def from_dict(dict: Dict[str, any]) -> Column:
    return Column(dict[Column.TECH_NAME_DICT_KEY], dict[Column.DESCRIPTION_DICT_KEY], dict[Column.ALLOWED_FOR_ENUM], dict[Column.NAME_DICT_KEY], dict[Column.NEED_PERCENT_CONVERT_DICT_KEY])

  @staticmethod
  def from_sr(sr: pd.Series) -> Column:
    return Column.from_dict(sr.to_dict())
