from .column import Column, ColType
import pandas as pd
from typing import List

all_columns = [
    Column("fundamental_currency_code", "Currency of metrics",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Metric currency"),
    Column("volume", "Trading volume per 1 day",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK],  "Volume / 1D"),
    Column("change", "Price change in 1 day, 0.01 = 1%",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Price change/1D mult", True),
    Column("market_cap_basic", "Market capitalization",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Market cap"),
    Column("type", "Type of element",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK]),
    Column("description", "Description of element",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK]),
    Column("dividends_yield_current", "Dividend per share / share price, 0.01 = 1%",
           [ColType.STOCK], "Dividend yield Mult TTM", True),
    Column("dividends_yield", "Dividend per share / share price FWD, 0.01 = 1%",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK], "Dividend yield Mult FWD", True),
    Column("price_book_fq", "Price of share / Book ratio of company, 0.01 = 1%",
           [ColType.STOCK], "Price/BookRatio"),
    Column("name", "Name of element",
           [ColType.INDUSTRY, ColType.SECTOR, ColType.STOCK]),
    Column("close", "Close price",
           [ColType.STOCK]),
    Column("pricescale", "Price decimal max lenght",
           [ColType.STOCK], "Decimal Len"),
    Column("currency", "Currency of price",
           [ColType.STOCK], "Currency"),
    Column("change_abs", "Change of price / 1 day in currency value",
           [ColType.STOCK], "Change in Cur / 1D"),
    Column("Value.Traded", "Capital traded / 1 day",
           [ColType.STOCK],  "Volume * Price / 1D"),
    Column("price_earnings_ttm", "Price / earning per 1 share",
           [ColType.STOCK], "Price/EarningPerShare"),
    Column("earnings_per_share_basic_ttm", "Earning per 1 share",
           [ColType.STOCK], "BasicEarningPerShare"),
    Column("dps_common_stock_prim_issue_fy", "Dividended per share",
           [ColType.STOCK], "Dividend/Share"),
    Column("market", "Market of element",
           [ColType.INDUSTRY, ColType.SECTOR], "Market"),
    Column("basic_elements", "Stocks in element",
           [ColType.INDUSTRY, ColType.SECTOR], "Stocks"),
    Column("sector", "Sector of element",
           [ColType.INDUSTRY, ColType.STOCK], "Sector"),
    Column("industry", "Industry of element",
           [ColType.STOCK], "Industry"),
    Column("elements", "Count of industries in element",
           [ColType.SECTOR], "Industries")
]

stock_columns = [c for c in all_columns if c.is_allowed_for(ColType.STOCK)]
industry_columns = [
    c for c in all_columns if c.is_allowed_for(ColType.INDUSTRY)]
sector_columns = [c for c in all_columns if c.is_allowed_for(ColType.SECTOR)]


def to_df(column_list: List[Column]) -> pd.DataFrame:
    return pd.DataFrame([c.to_dict() for c in column_list]).sort_values(Column.NAME_DICT_KEY).reset_index(drop=True)
