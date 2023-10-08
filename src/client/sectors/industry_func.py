import pandas as pd

from ..columns.column_type import ColumnType
from ...api.scan_api import post_scan, SymbolQueryTypes, RequestContext, Filter
from ..columns.columns import List, Column
from ..tool.request_tool import parse_json, check_columns, Response


def get_industries_overview(columns: List[Column] = list(Column.column_dic_for(ColumnType.INDUSTRY).keys()), request_context: RequestContext = RequestContext()) -> Response:
    check_columns(request_context, columns, ColumnType.INDUSTRY)
    response_json = post_scan([c.value for c in columns], request_context,
                              SymbolQueryTypes.INDUSTRY)
    return parse_json(columns, response_json)
