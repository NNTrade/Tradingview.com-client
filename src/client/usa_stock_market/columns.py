from __future__ import annotations
from ...api.symbol_query_types import SymbolQueryTypes
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


class ColumnInfo:
    def __init__(self, col_enum: Column, description: str, allowedFor: List[ColType], output: str = None, needPercentConvert: bool = False) -> None:
        if len(allowedFor) == 0:
            raise Exception("Column must be allowed at least for one client")
        self.__allowedFor = allowedFor
        self.__descripion = description
        self.__tech_name = col_enum.value
        self.__name = col_enum
        self.__output = output if output is not None else col_enum.value.capitalize()
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
    def enum(self) -> Column:
        return self.__name

    @property
    def tech_name(self) -> str:
        return self.__tech_name

    @property
    def output_name(self) -> str:
        return self.__output

    @property
    def needPercentConvert(self) -> str:
        return self.__needPercentConvert

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, ColumnInfo):
            return False

        return self.output_name == __value.output_name and \
            self.tech_name == __value.tech_name and \
            self.needPercentConvert == __value.needPercentConvert and \
            len(self.__allowedFor) == len(
                __value.__allowedFor) and self.__allowedFor == __value.__allowedFor
    ENUM_DICT_KEY = "ENUM"
    TECH_NAME_DICT_KEY = "Tech name"
    DESCRIPTION_DICT_KEY = "Description"
    OUTPUT_NAME_DICT_KEY = "Output name"
    NEED_PERCENT_CONVERT_DICT_KEY = "Need percent convert"
    ALLOWED_FOR = "Allowed for"
    ALLOWED_FOR_ENUM = "Allowed for enum"

    def to_dict(self) -> Dict[str, any]:
        return {ColumnInfo.ENUM_DICT_KEY: self.enum,
                ColumnInfo.OUTPUT_NAME_DICT_KEY: self.output_name,
                ColumnInfo.TECH_NAME_DICT_KEY: self.tech_name,
                ColumnInfo.DESCRIPTION_DICT_KEY: self.description,
                ColumnInfo.NEED_PERCENT_CONVERT_DICT_KEY: self.needPercentConvert,
                ColumnInfo.ALLOWED_FOR: [e.value for e in self.allowedFor],
                ColumnInfo.ALLOWED_FOR_ENUM: self.allowedFor}

    @staticmethod
    def from_dict(dict: Dict[str, any]) -> ColumnInfo:
        return ColumnInfo(dict[ColumnInfo.TECH_NAME_DICT_KEY], dict[ColumnInfo.DESCRIPTION_DICT_KEY], dict[ColumnInfo.ALLOWED_FOR_ENUM], dict[ColumnInfo.OUTPUT_NAME_DICT_KEY], dict[ColumnInfo.NEED_PERCENT_CONVERT_DICT_KEY])

    @staticmethod
    def from_sr(sr: pd.Series) -> ColumnInfo:
        sr_dict = sr.to_dict()
        if ColumnInfo.ENUM_DICT_KEY not in sr_dict.keys() and isinstance(sr.name, Column):
            sr_dict[ColumnInfo.ENUM_DICT_KEY] = sr.name
        return ColumnInfo.from_dict(sr_dict)


class Column(Enum):
    metric_cur = "fundamental_currency_code"
    volume = "volume"
    price_change_per_1d = "change"
    market_cap = "market_cap_basic"
    type = "type"
    description = "description"
    dividends_yield_current = "dividends_yield_current"
    dividends_yield_fwd = "dividends_yield"
    price_vs_bookratio = "price_book_fq"
    el_name = "name"
    close = "close"
    price_dec_len = "pricescale"
    currency = "currency"
    price_change_abs = "change_abs"
    TradedCap = "Value.Traded"
    price_vs_earnings_per_share = "price_earnings_ttm"
    earnings_per_share = "earnings_per_share_basic_ttm"
    dividend_per_share = "dps_common_stock_prim_issue_fy"
    market_country = "market"
    stocks = "basic_elements"
    sector = "sector"
    industry = "industry"
    cnt_industries = "elements"
    market = "exchange"

    @staticmethod
    def all_column_info() -> List[ColumnInfo]:
        return columns_info

    @staticmethod
    def all_column_info_dic() -> Dict[Column, ColumnInfo]:
        return {c.enum: c for c in Column.all_column_info()}

    @staticmethod
    def stock_column_dic() -> Dict[Column, ColumnInfo]:
        return {c.enum: c for c in Column.all_column_info() if c.is_allowed_for(ColType.STOCK)}

    @staticmethod
    def industry_column_dic() -> Dict[Column, ColumnInfo]:
        return {
            c.enum: c for c in Column.all_column_info() if c.is_allowed_for(ColType.INDUSTRY)}

    @staticmethod
    def sector_column_dic() -> Dict[Column, ColumnInfo]:
        return {c.enum: c for c in Column.all_column_info() if c.is_allowed_for(ColType.SECTOR)}

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.value != other.value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.value < other.value
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.value > other.value
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.value <= other.value
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.value >= other.value
        return NotImplemented

    def __hash__(self):
        return hash(self.value)


def to_df(column_list: List[ColumnInfo]) -> pd.DataFrame:
    return pd.DataFrame([c.to_dict() for c in column_list]).set_index(ColumnInfo.ENUM_DICT_KEY).sort_index()


columns_info = [
    ColumnInfo(Column.metric_cur, "Currency of metrics",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Metric currency"),
    ColumnInfo(Column.volume, "Trading volume per 1 day",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK],  "Volume / 1D"),
    ColumnInfo(Column.price_change_per_1d, "Price change in 1 day, 0.01 = 1%",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Price change/1D mult", True),
    ColumnInfo(Column.market_cap, "Market capitalization",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Market cap"),
    ColumnInfo(Column.type, "Type of element",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK]),
    ColumnInfo(Column.description, "Description of element",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK]),
    ColumnInfo(Column.dividends_yield_current, "Dividend per share / share price, 0.01 = 1%",
               [ColType.STOCK], "Dividend yield Mult TTM", True),
    ColumnInfo(Column.dividends_yield_fwd, "Dividend per share / share price FWD, 0.01 = 1%",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Dividend yield Mult FWD", True),
    ColumnInfo(Column.price_vs_bookratio, "Price of share / Book ratio of company, 0.01 = 1%",
               [ColType.STOCK], "Price/BookRatio"),
    ColumnInfo(Column.el_name, "Name of element",
               [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK]),
    ColumnInfo(Column.close, "Close price",
               [ColType.STOCK]),
    ColumnInfo(Column.price_dec_len, "Price decimal max lenght",
               [ColType.STOCK], "Price decimal Len"),
    ColumnInfo(Column.currency, "Currency of price",
               [ColType.STOCK], "Currency"),
    ColumnInfo(Column.price_change_abs, "Change of price / 1 day in currency value",
               [ColType.STOCK], "Change in Cur / 1D"),
    ColumnInfo(Column.TradedCap, "Capital traded / 1 day",
               [ColType.STOCK],  "Volume * Price / 1D"),
    ColumnInfo(Column.price_vs_earnings_per_share, "Price / earning per 1 share",
               [ColType.STOCK], "Price/EarningPerShare"),
    ColumnInfo(Column.earnings_per_share, "Earning per 1 share",
               [ColType.STOCK], "BasicEarningPerShare"),
    ColumnInfo(Column.dividend_per_share, "Dividended per share",
               [ColType.STOCK], "Dividend/Share"),
    ColumnInfo(Column.market_country, "Market country of element",
               [ColType.INDUSTRY, ColType.SECTOR], "Market country"),
    ColumnInfo(Column.stocks, "Stocks in element",
               [ColType.INDUSTRY, ColType.SECTOR], "Stocks"),
    ColumnInfo(Column.sector, "Sector of element",
               [ColType.INDUSTRY, ColType.STOCK], "Sector"),
    ColumnInfo(Column.industry, "Industry of element",
               [ColType.STOCK], "Industry"),
    ColumnInfo(Column.cnt_industries, "Count of industries in element",
               [ColType.SECTOR], "Industries"),
    ColumnInfo(Column.market, "Market of stock trading",
               [ColType.STOCK], output="Market")
]
