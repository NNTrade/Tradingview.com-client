from typing import Tuple
import pandas as pd
from ...api.scan_api import post_scan, SymbolQueryTypes, RequestContext, Filter
from .columns.column_list import List, stock_column_dic
from .__tools import parse_json, check_columns, ColType, Response
from .columns.column import Column


def __get_stocks(columns: List[str] = list(stock_column_dic.keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColType.STOCK)
    response_json = post_scan(columns, request_context)
    return parse_json(columns, response_json)


def get_stocks(columns: List[str] = list(stock_column_dic.keys()), request_context: RequestContext = RequestContext()) -> Response:
    return __get_stocks(columns, request_context)


def get_sector_stocks(sector_name: str,
                      columns: List[str] = list(stock_column_dic.keys()),
                      request_context: RequestContext = RequestContext()) -> Response:
    request_context = request_context.clone()
    request_context.filters.append(
        Filter(SymbolQueryTypes.SECTOR.value, Filter.CompareFunc.eq, sector_name))
    return __get_stocks(columns, request_context)


def get_industry_stocks(industry_name: str,
                        columns: List[str] = list(stock_column_dic.keys()),
                        request_context: RequestContext = RequestContext()) -> Response:
    request_context = request_context.clone()
    request_context.filters.append(
        Filter(SymbolQueryTypes.INDUSTRY.value, Filter.CompareFunc.eq, industry_name))
    return __get_stocks(columns, request_context)


def get_stock_by(type: SymbolQueryTypes, name: str,
                 columns: List[str] = list(stock_column_dic.keys()),
                 request_context: RequestContext = RequestContext()) -> Response:
    if type == SymbolQueryTypes.SECTOR:
        return get_sector_stocks(name, columns, request_context)
    elif type == SymbolQueryTypes.INDUSTRY:
        return get_industry_stocks(name, columns, request_context)
    else:
        raise Exception("Unespected SymbolQueryTypes")


def get_stock_by_series(area_sr: pd.Series,
                        columns: List[str] = list(stock_column_dic.keys()),
                        request_context: RequestContext = RequestContext()) -> Response:
    return get_stock_by(SymbolQueryTypes(area_sr["Type"]), area_sr["Description"], columns, request_context)
