from ..exceptions import UnparsableNumber
import numpy as np
import pandas as pd

pow_exp_dict = {"%": -2, "K": 3, "M": 6, "B": 9, "T": 12, "Q": 15}


def parse_number(str_value: str) -> float:
  str_value = str_value.replace("−", "-")
  last_char = str_value[-1:]

  try:
    if last_char.isdigit():
      return float(str_value)
    elif last_char == "−" or last_char == "-" or last_char == "—":
      return np.NaN
    pow_exp = pow_exp_dict.get(last_char)

    if pow_exp is not None:
      return float(str_value[:-1])*pow(10, pow_exp)

  except ValueError:
    raise UnparsableNumber(str_value)

  raise UnparsableNumber(str_value)


def convert_percent_to_mult(df: pd.DataFrame) -> pd.DataFrame:
  return df.applymap(lambda el: el/100)
