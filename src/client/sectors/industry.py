from __future__ import annotations
from typing import List, Union
import pandas as pd
from ..columns import Column, ColumnType
from ...api.scan_api import RequestContext
from ...api import MarketEnum
from ..stocks.stock_func import get_industry_stocks, Response
from .industry_func import get_industries_overview


class IndustriesSource:
    @staticmethod
    def of(market: MarketEnum) -> IndustriesSource:
        request_context: RequestContext = RequestContext()
        request_context.market = market
        return IndustriesSource(request_context)

    def __init__(self, request_context: RequestContext) -> None:
        self.request_context = request_context
        pass

    def get_overview(self, columns: List[Column] = None) -> Response:
        if columns is None:
            columns = list(Column.column_dic_for(ColumnType.INDUSTRY).keys())
        return get_industries_overview(columns, self.request_context)

    def get_industry(self, industry: Union[str, pd.Series], clone_context: bool = False) -> Industry:
        """Get industry

        Args:
            industry (Union[str, pd.Series]): Value from Sector Column.description or pandas DataFrame row from get_overview
            clone_context (bool, optional): Clone currenct RequestContext. Defaults to False.

        Returns:
            Industry: industry
        """
        next_context = self.request_context.clone(
        ) if clone_context else self.request_context
        if isinstance(industry, pd.Series):
            industry = industry[Column.description.get_info(
            ).output_name]
        return Industry(industry, next_context)


class Industry:
    def __init__(self, industry: str, request_context: RequestContext) -> None:
        self.request_context = request_context
        self.industry = industry
        pass

    def get_stocks(self, columns: List[Column] = None) -> Response:
        if columns is None:
            columns = list(Column.column_dic_for(ColumnType.STOCK).keys())
        return get_industry_stocks(self.industry, columns, self.request_context)
