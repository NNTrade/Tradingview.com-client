from typing import List
from .columns.column_list import Column, ColType


class WrongColumnsException(Exception):
  def __init__(self, wrongColList: List[Column], type: ColType) -> None:
    super().__init__(
        f"Column{'s' if len(wrongColList) > 1 else ''} doesn't allowed for {type.value}: {', '.join([c.name for c in wrongColList])}")
