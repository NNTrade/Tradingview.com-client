from typing import List, Dict
import pandas as pd


def scan_json_parse(column: List[str], payload_json: Dict) -> pd.DataFrame:
  idx = [row["s"] for row in payload_json["data"]]
  data_arr = [row["d"] for row in payload_json["data"]]
  _ret_df = pd.DataFrame(data_arr, columns=column, index=idx)
  _ret_df.index.name = "Id"
  return _ret_df
