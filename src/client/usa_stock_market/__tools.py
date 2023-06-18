import pandas as pd
from ...api.scan_api import Dict
from ...parser.scan_json_parser import scan_json_parse
from ...parser.number_parser import convert_df_with_percent_into_df_of_mult
from typing import List
from .columns import ColumnInfo, ColType, Column
from .exceptions import WrongColumnsException
from .response import Response
from ...api.request_context import RequestContext


def parse_json(cols: List[Column], response_json: Dict) -> Response:
    _ret_df = scan_json_parse([c.value for c in cols], response_json)
    all_col_dict = Column.all_column_info_dic()
    pers_col = []
    rename = {}
    for c in cols:
        column_info = all_col_dict[c]
        if column_info.needPercentConvert:
            pers_col.append(c.value)
        rename[c.value] = column_info.output_name
    _ret_df[pers_col] = convert_df_with_percent_into_df_of_mult(
        _ret_df[pers_col])

    _ret_df.rename(columns=rename, inplace=True)

    return Response(int(response_json["totalCount"]), _ret_df)


def check_columns(request_context: RequestContext, columns: List[Column], checkedType: ColType):
    all_col_dict = Column.all_column_info_dic()
    wrong_col = []
    for c in columns:
        col = all_col_dict.get(c)
        if col is None or not col.is_allowed_for(checkedType):
            wrong_col.append(c.name)
    for filter in request_context.filters:
        __check_str_field(wrong_col, filter.field, all_col_dict, checkedType)
    __check_str_field(wrong_col, request_context.sort.field,
                      all_col_dict, checkedType)
    if len(wrong_col) > 0:
        raise WrongColumnsException(wrong_col, checkedType)


def __check_str_field(wrong_col: List[str], field: str, all_col_dict: Dict[Column, ColumnInfo], checkedType: ColType):
    try:
        col = all_col_dict.get(Column(field))

        if col is None or not col.is_allowed_for(checkedType):
            wrong_col.append(field)
    except ValueError:
        wrong_col.append(field)
