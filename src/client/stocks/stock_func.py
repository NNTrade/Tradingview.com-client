import pandas as pd

from ..columns.column_type import ColumnType
from ...api.scan_api import post_scan, SymbolQueryTypes, RequestContext, Filter
from ..columns.columns import List, Column
from ..tool.request_tool import parse_json, check_columns, Response


def __get_stocks(columns: List[Column] = list(Column.column_dic_for(ColumnType.STOCK).keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColumnType.STOCK)
    response_json = post_scan([c.value for c in columns], request_context)
    return parse_json(columns, response_json)


def get_stocks_overview(columns: List[Column] = list(Column.column_dic_for(ColumnType.STOCK).keys()), request_context: RequestContext = RequestContext()) -> Response:
    return __get_stocks(columns, request_context)


def get_sector_stocks(sector_name: str,
                      columns: List[Column] = list(
                          Column.column_dic_for(ColumnType.STOCK).keys()),
                      request_context: RequestContext = RequestContext()) -> Response:
    request_context = request_context.clone()
    request_context.filters.append(
        Filter(SymbolQueryTypes.SECTOR.value, Filter.CompareFunc.eq, sector_name))
    return __get_stocks(columns, request_context)


def get_industry_stocks(industry_name: str,
                        columns: List[Column] = list(
                            Column.column_dic_for(ColumnType.STOCK).keys()),
                        request_context: RequestContext = RequestContext()) -> Response:
    request_context = request_context.clone()
    request_context.filters.append(
        Filter(SymbolQueryTypes.INDUSTRY.value, Filter.CompareFunc.eq, industry_name))
    return __get_stocks(columns, request_context)


def get_stock_by(type: SymbolQueryTypes, name: str,
                 columns: List[Column] = list(
                     Column.column_dic_for(ColumnType.STOCK).keys()),
                 request_context: RequestContext = RequestContext()) -> Response:
    if type == SymbolQueryTypes.SECTOR:
        return get_sector_stocks(name, columns, request_context)
    elif type == SymbolQueryTypes.INDUSTRY:
        return get_industry_stocks(name, columns, request_context)
    else:
        raise Exception("Unespected SymbolQueryTypes")


def get_stock_by_series(area_sr: pd.Series,
                        columns: List[Column] = list(
                            Column.column_dic_for(ColumnType.STOCK).keys()),
                        request_context: RequestContext = RequestContext()) -> Response:
    return get_stock_by(SymbolQueryTypes(area_sr["Type"]), area_sr["Description"], columns, request_context)
