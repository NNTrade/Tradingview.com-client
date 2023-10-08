from typing import List

from . import ColumnInfo, ColumnType


class WrongColumnsException(Exception):
  def __init__(self, wrongColList: List[str], type: ColumnType) -> None:
    super().__init__(
        f"Column{'s' if len(wrongColList) > 1 else ''} doesn't allowed for {type.value}: {', '.join(wrongColList)}")
