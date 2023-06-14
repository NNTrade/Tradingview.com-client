import pandas as pd
from ...api.scan_api import post_scan, SymbolQueryTypes
from .columns.column_set import sector_columns, industry_columns
from .columns.column import Column
from .parse_json import parse_json


def get_sectors(top_order: Column = sector_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    response_json = post_scan([c.tech_name for c in sector_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, SymbolQueryTypes.SECTOR)
    return parse_json(sector_columns, response_json)


def get_industries(top_order: Column = industry_columns[0], get_top: int = 200, start_top_from: int = 0,  top_asc: bool = True) -> pd.DataFrame:
    response_json = post_scan([c.tech_name for c in industry_columns], get_top,
                              start_top_from, top_order.tech_name, top_asc, SymbolQueryTypes.INDUSTRY)
    return parse_json(industry_columns, response_json)
