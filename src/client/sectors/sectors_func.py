from ...api.scan_api import RequestContext, SymbolQueryTypes, post_scan, Filter
from ..columns.column_type import ColumnType
from ..columns.columns import Column, List
from ..tool.request_tool import Response, check_columns, parse_json


def get_sectors_overview(columns: List[Column] = list(Column.column_dic_for(ColumnType.SECTOR).keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColumnType.SECTOR)
    response_json = post_scan(
        [c.value for c in columns], request_context, SymbolQueryTypes.SECTOR)
    return parse_json(columns, response_json)


def get_industries_overview_of_sector(sector: str, columns: List[Column] = list(Column.column_dic_for(ColumnType.INDUSTRY).keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColumnType.INDUSTRY)
    response_json = post_scan([c.value for c in columns], request_context,
                              SymbolQueryTypes.INDUSTRY, [Filter.EQ(SymbolQueryTypes.SECTOR.value, sector)])
    return parse_json(columns, response_json)
