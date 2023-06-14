class DoesNotResponseException(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)


class UnparsableNumber(Exception):
  def __init__(self, string_value: str) -> None:
    super().__init__(f"Cann't parse numebre {string_value}")
