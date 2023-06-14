from typing import List, Tuple
from bs4 import BeautifulSoup, ResultSet
import pandas as pd


def parse_header_from_soup(soup: BeautifulSoup) -> List[str]:
    table_headers = soup.select("table thead th")

    # Extract the column names
    column_names = [header.text.strip() for header in table_headers]

    return column_names


def parse_header_from_payload(response_data: str) -> List[str]:
    soup = BeautifulSoup(response_data, 'html.parser')
    return parse_header_from_soup(soup)


def get_soup_from_payload(payload: str) -> BeautifulSoup:
    return BeautifulSoup(payload.replace("\n", ""), 'html.parser')


def parse_cells_from_soup(soup: BeautifulSoup) -> List[List[ResultSet]]:
    return [row.find_all("td") for row in soup.select("table tbody tr")]


def parse_data_from_soup(soup: BeautifulSoup) -> List[List[str]]:
    ret_rows = []
    for row in soup.select("table tbody tr"):
        row_cells = row.find_all("td")
        ret_rows.append([cell.text.strip() for cell in row_cells])
    return ret_rows


def parse_data_from_payload(response_data: str) -> List[List[str]]:
    soup = BeautifulSoup(response_data, 'html.parser')

    return parse_data_from_soup(soup)


def parse_currency_columns(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    ret_cur_arr = []
    ret_val_arr = []
    for col in df.columns:
        (val_sr, cur_sr) = parse_currency_column(df[col])
        cur_sr.name = col
        val_sr.name = col
        ret_cur_arr.append(cur_sr)
        ret_val_arr.append(val_sr)
    return pd.DataFrame(ret_val_arr).T, pd.DataFrame(ret_cur_arr).T


def parse_currency_column(sr: pd.Series) -> Tuple[pd.Series, pd.Series]:
    splitted_df = sr.str.split(" ", expand=True)
    return splitted_df[0], splitted_df[1]


def parse_urls(df: pd.DataFrame) -> pd.DataFrame:
   return df.applymap(lambda el: el.find('a')['href'])

