import pandas as pd
from typing import List
from bs4 import BeautifulSoup
import numpy as np
from typing import Tuple
from .number_parser import parse_number
from ._parse_tools import parse_header_from_soup, get_soup_from_payload, parse_data_from_soup

currency_columns = ["Market cap"]


def parse_urls_from_soup(soup: BeautifulSoup) -> List[str]:
    return [link['href'] for link in soup.select('tbody tr td:first-child a')]


def parse_currency_columns(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    ret_cur_arr = []
    for col in currency_columns:
        if col in df.columns:
            (df[col], cur_sr) = parse_currency_column(df[col])
            cur_sr.name = col
            ret_cur_arr.append(cur_sr)
    return df, pd.DataFrame(ret_cur_arr).T


def parse_currency_column(sr: pd.Series) -> Tuple[pd.Series, pd.Series]:
    splitted_df = sr.str.split(" ", expand=True)
    return splitted_df[0], splitted_df[1]


def trim(str_value: str) -> str:
    return ' '.join(str_value.split())


def sectors_response_parse(response_data: str) -> pd.DataFrame:
    soup = get_soup_from_payload(response_data)
    cols = parse_header_from_soup(soup)
    rows = parse_data_from_soup(soup)

    _ret_df = pd.DataFrame([row[1:] for row in rows], columns=[col.replace("%", "rel") for col in cols[1:]], index=[
                           trim(row[0]) for row in rows]).rename_axis(cols[0])

    (_ret_df, cur_df) = parse_currency_columns(_ret_df)

    _ret_df = _ret_df.applymap(lambda el: parse_number(el))

    url_sr = pd.Series([link['href'] for link in soup.select(
        'tbody tr td:first-child a')], index=_ret_df.index).rename("Sector stocks URL")

    return _ret_df.join(cur_df, rsuffix=" currency").join(url_sr)
