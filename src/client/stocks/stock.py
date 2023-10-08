from __future__ import annotations
from ...api.scan_api import RequestContext
from ...api import MarketEnum
from typing import List
from ..columns import Column, ColumnType
from .stock_func import get_stocks_overview, Response


class StockSource:
    @staticmethod
    def of(market: MarketEnum) -> StockSource:
        request_context: RequestContext = RequestContext()
        request_context.market = market
        return StockSource(request_context)

    def __init__(self, request_context: RequestContext) -> None:
        self.request_context = request_context
        pass

    def get_overview(self, columns: List[Column] = None) -> Response:
        if columns is None:
            columns = list(Column.column_dic_for(ColumnType.STOCK).keys())
        return get_stocks_overview(columns, self.request_context)
