import pandas as pd
from ...api.scan_api import post_scan, SymbolQueryTypes, RequestContext
from .columns import List, Column, ColType
from .__tools import parse_json, check_columns, Response


def get_sectors(columns: List[Column] = list(Column.sector_column_dic().keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColType.SECTOR)
    response_json = post_scan(
        [c.value for c in columns], request_context, SymbolQueryTypes.SECTOR)
    return parse_json(columns, response_json)


def get_industries(columns: List[Column] = list(Column.industry_column_dic().keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColType.INDUSTRY)
    response_json = post_scan([c.value for c in columns], request_context,
                              SymbolQueryTypes.INDUSTRY)
    return parse_json(columns, response_json)
