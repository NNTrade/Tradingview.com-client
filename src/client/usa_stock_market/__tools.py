import pandas as pd
from ...api.scan_api import Dict
from ...parser.scan_json_parser import scan_json_parse
from ...parser.number_parser import convert_percent_to_mult
from typing import List
from .columns.column_list import Column, ColType, all_column_dic
from .exceptions import WrongColumnsException
from .response import Response
from ...api.request_context import RequestContext


def parse_json(cols: List[str], response_json: Dict) -> Response:
    _ret_df = scan_json_parse(cols, response_json)
    pers_col = []
    rename = {}
    for c in cols:
        column_info = all_column_dic[c]
        if column_info.needPercentConvert:
            pers_col.append(c)
        rename[c] = column_info.output_name
    _ret_df[pers_col] = convert_percent_to_mult(_ret_df[pers_col])

    _ret_df.rename(columns=rename, inplace=True)

    return Response(int(response_json["totalCount"]), _ret_df)


def check_columns(request_context: RequestContext, columns: List[str], checkedType: ColType):

    wrong_col = []
    for c in columns:
        col = all_column_dic.get(c)
        if col is None or not col.is_allowed_for(checkedType):
            wrong_col.append(c)
    for filter in request_context.filters:
        col = all_column_dic.get(filter.field)
        if col is None or not col.is_allowed_for(checkedType):
            wrong_col.append(filter.field)

    if len(wrong_col) > 0:
        raise WrongColumnsException(wrong_col, checkedType)
