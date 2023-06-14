import pandas as pd
from ._parse_tools import parse_header_from_soup, get_soup_from_payload, parse_cells_from_soup, parse_currency_columns, parse_urls
from .number_parser import parse_number
from typing import List, Dict

_currency_columns = ["Market cap"]
_url_columns = ["Industry", "Sector"]
_no_value_columns = ["Industry", "Sector"]


def industry_response_parse(response_data: str) -> pd.DataFrame:
  soup = get_soup_from_payload(response_data)
  cols = parse_header_from_soup(soup)
  rows = parse_cells_from_soup(soup)

  cols = [c.replace("%", "rel") for c in cols]

  cells_df = pd.DataFrame(rows, columns=cols)

  value_df = cells_df.applymap(lambda el: el.text.strip())

  value_df[_currency_columns], cur_df = parse_currency_columns(
      value_df[_currency_columns])

  url_df = parse_urls(cells_df[_url_columns])

  value_df = value_df.applymap(lambda el: ' '.join(el.split()))

  value_col = [c for c in cols if c not in _no_value_columns]
  value_df[value_col] = value_df[value_col].applymap(
      lambda el: parse_number(el))

  _ret_df = value_df.join(cur_df, rsuffix=" currency").join(
      url_df, rsuffix=" URL").set_index("Industry")
  return _ret_df
