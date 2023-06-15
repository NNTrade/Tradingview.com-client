from typing import List
from .columns import ColumnInfo, ColType


class WrongColumnsException(Exception):
  def __init__(self, wrongColList: List[str], type: ColType) -> None:
    super().__init__(
        f"Column{'s' if len(wrongColList) > 1 else ''} doesn't allowed for {type.value}: {', '.join(wrongColList)}")
