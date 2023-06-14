import pandas as pd
from ...api.scan_api import post_scan, SymbolQueryTypes
from .columns.column_set import stock_columns
from .parse_json import parse_json
from .columns.column import Column


def get_stocks(top_order: Column = stock_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    response_json = post_scan([c.tech_name for c in stock_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, None)
    return parse_json(stock_columns, response_json)


def get_sector_stocks(sector_name: str, top_order:  Column = stock_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    response_json = post_scan([c.tech_name for c in stock_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, None, (SymbolQueryTypes.SECTOR, sector_name))
    return parse_json(stock_columns, response_json)


def get_industry_stocks(industry_name: str, top_order:  Column = stock_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    response_json = post_scan([c.tech_name for c in stock_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, None, (SymbolQueryTypes.INDUSTRY, industry_name))
    return parse_json(stock_columns, response_json)


def get_stock_by(type: SymbolQueryTypes, name: str, top_order: Column = stock_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    if type == SymbolQueryTypes.SECTOR:
        return get_sector_stocks(name, top_order, get_top, start_top_from, top_asc)
    elif type == SymbolQueryTypes.INDUSTRY:
        return get_industry_stocks(name, top_order, get_top, start_top_from, top_asc)
    else:
        raise Exception("Unespected SymbolQueryTypes")


def get_stock_by_series(area_sr: pd.Series, top_order: Column = stock_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    return get_stock_by(SymbolQueryTypes(area_sr["type"]), area_sr["description"], top_order, get_top, start_top_from, top_asc)
