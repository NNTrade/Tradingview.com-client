import pandas as pd


class Response:
  def __init__(self, total_count: int, loaded_df: pd.DataFrame):
    self.total_count = total_count
    self.loaded_df = loaded_df
