import pandas as pd
from ...api.scan_api import Dict
from ...parser.scan_json_parser import scan_json_parse
from ...parser.number_parser import convert_percent_to_mult
from typing import List
from .columns.column_list import Column, ColType
from .exceptions import WrongColumnsException


def parse_json(cols: List[Column], response_json: Dict) -> pd.DataFrame:
    _ret_df = scan_json_parse([c.tech_name for c in cols], response_json)
    _ret_df[[c.tech_name for c in cols if c.needPercentConvert]] = convert_percent_to_mult(
        _ret_df[[c.tech_name for c in cols if c.needPercentConvert]])

    _ret_df.rename(columns={c.tech_name: c.name for c in cols}, inplace=True)

    return _ret_df


def check_columns(top_order: Column, columns: List[Column], checkedType: ColType):
    wrong_col = [c for c in columns if not c.is_allowed_for(checkedType)]
    if len(wrong_col) > 0:
        raise WrongColumnsException(wrong_col, checkedType)
    if not top_order.is_allowed_for(checkedType):
        raise WrongColumnsException([top_order], checkedType)
