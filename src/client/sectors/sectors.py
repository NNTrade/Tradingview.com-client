from __future__ import annotations
from typing import List, Union
from .industry import Industry, IndustriesSource
from ..columns import Column, ColumnType
from ...api.scan_api import RequestContext
from ...api import MarketEnum
from ..tool import Response
from .sectors_func import get_sectors_overview, get_industries_overview_of_sector
from ..stocks.stock_func import get_sector_stocks
import pandas as pd


class SectorsSource:
    @staticmethod
    def of(market: MarketEnum) -> SectorsSource:
        request_context: RequestContext = RequestContext()
        request_context.market = market
        return SectorsSource(request_context)

    def __init__(self, request_context: RequestContext) -> None:
        self.request_context = request_context
        pass

    def get_overview(self, columns: List[Column] = None) -> Response:
        if columns is None:
            columns = list(Column.column_dic_for(ColumnType.SECTOR).keys())
        return get_sectors_overview(columns, self.request_context)

    def get_sector(self, sector: Union[str, pd.Series], clone_context: bool = False) -> Sector:
        """Get sector

        Args:
            sector (Union[str, pd.Series]): Value from Sector Column.description or pandas DataFrame row from get_overview
            clone_context (bool, optional): Clone currenct RequestContext. Defaults to False.

        Returns:
            Sector: Sector
        """
        next_context = self.request_context.clone(
        ) if clone_context else self.request_context
        if isinstance(sector, pd.Series):
            sector = sector[Column.description.get_info(
            ).output_name]
        return Sector(sector, next_context)


class Sector:
    def __init__(self, sector: str, request_context: RequestContext) -> None:
        self.request_context = request_context
        self.sector = sector
        pass

    def get_industries(self, columns: List[Column] = None) -> Response:
        if columns is None:
            columns = list(
                Column.column_dic_for(ColumnType.INDUSTRY).keys())
        return get_industries_overview_of_sector(self.sector, columns, self.request_context)

    def get_stocks(self, columns: List[Column] = None) -> Response:
        if columns is None:
            columns = list(Column.column_dic_for(ColumnType.STOCK).keys())
        return get_sector_stocks(self.sector, columns, self.request_context)

    def get_industry(self, industry: Union[str, pd.Series], clone_context: bool = False) -> Industry:
        """Get industry

        Args:
            industry (Union[str, pd.Series]): Value from Sector Column.description or pandas DataFrame row from get_overview
            clone_context (bool, optional): Clone currenct RequestContext. Defaults to False.

        Returns:
            Industry: industry
        """
        if isinstance(industry, pd.Series):
            industry = industry[Column.description.get_info(
            ).output_name]
        return IndustriesSource(self.request_context).get_industry(industry, clone_context)
