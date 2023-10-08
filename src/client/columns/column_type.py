from ...api.symbol_query_types import SymbolQueryTypes
from enum import Enum


class ColumnType(Enum):
    """
    Enum of column Types.
    Indicates in which metric type column could be getted
    """
    INDUSTRY = "industry"
    SECTOR = "sector"
    STOCK = "stock"

    #def toSymbolQueryTypes(self) -> SymbolQueryTypes:
    #    if self != ColumnType.STOCK:
    #        return SymbolQueryTypes(self.value)
    #    return None
