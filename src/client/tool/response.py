import pandas as pd
import logging


class Response:
  def __init__(self, total_count: int, loaded_df: pd.DataFrame):
    if total_count > len(loaded_df):
      logging.getLogger("Response").warning(
          "Not all records has been loaded. Loaded %i records of %i", len(loaded_df), total_count)
    self.total_count = total_count
    self.loaded_df = loaded_df
