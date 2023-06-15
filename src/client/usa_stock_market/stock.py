from typing import Tuple
import pandas as pd
from ...api.scan_api import post_scan, SymbolQueryTypes
from .columns.column_list import stock_columns, List
from .__tools import parse_json, check_columns, ColType
from .columns.column import Column


def __get_stocks(top_order: Column = stock_columns[0], columns: List[Column] = stock_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True, filter: Tuple[SymbolQueryTypes, str] = None) -> pd.DataFrame:
    check_columns(top_order, columns, ColType.STOCK)
    response_json = post_scan([c.tech_name for c in stock_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, None, filter)
    return parse_json(stock_columns, response_json)


def get_stocks(top_order: Column = stock_columns[0], columns: List[Column] = stock_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    return __get_stocks(top_order, columns, get_top, start_top_from, top_asc)


def get_sector_stocks(sector_name: str, top_order:  Column = stock_columns[0], columns: List[Column] = stock_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    return __get_stocks(top_order, columns, get_top, start_top_from, top_asc, (SymbolQueryTypes.SECTOR, sector_name))


def get_industry_stocks(industry_name: str, top_order:  Column = stock_columns[0], columns: List[Column] = stock_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    return __get_stocks(top_order, columns, get_top, start_top_from, top_asc, (SymbolQueryTypes.INDUSTRY, industry_name))


def get_stock_by(type: SymbolQueryTypes, name: str, top_order: Column = stock_columns[0], columns: List[Column] = stock_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    if type == SymbolQueryTypes.SECTOR:
        return get_sector_stocks(name, top_order,columns, get_top, start_top_from, top_asc)
    elif type == SymbolQueryTypes.INDUSTRY:
        return get_industry_stocks(name, top_order,columns, get_top, start_top_from, top_asc)
    else:
        raise Exception("Unespected SymbolQueryTypes")


def get_stock_by_series(area_sr: pd.Series, top_order: Column = stock_columns[0], columns: List[Column] = stock_columns,get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    return get_stock_by(SymbolQueryTypes(area_sr["Type"]), area_sr["Description"], top_order,columns, get_top, start_top_from, top_asc)
