import pandas as pd
from ...api.scan_api import post_scan, SymbolQueryTypes
from .columns.column_list import List, Column, sector_columns, industry_columns, ColType
from .__tools import parse_json, check_columns
from .exceptions import WrongColumnsException


def get_sectors(top_order: Column = sector_columns[0], columns: List[Column] = sector_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    check_columns(top_order,columns, ColType.SECTOR)
    response_json = post_scan([c.tech_name for c in columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, SymbolQueryTypes.SECTOR)
    return parse_json(sector_columns, response_json)


def get_industries(top_order: Column = industry_columns[0], columns: List[Column] = industry_columns, get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    check_columns(top_order,columns, ColType.INDUSTRY)
    response_json = post_scan([c.tech_name for c in industry_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, SymbolQueryTypes.INDUSTRY)
    return parse_json(industry_columns, response_json)
