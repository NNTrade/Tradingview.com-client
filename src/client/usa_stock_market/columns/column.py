class Column:
  def __init__(self, tech_name: str, rename: str = None, needPercentConvert: bool = False) -> None:
    self.__tech_name = tech_name
    self.__rename = rename if rename is not None else tech_name
    self.__needPercentConvert = needPercentConvert
    super().__init__()

  @property
  def tech_name(self) -> str:
    return self.__tech_name

  @property
  def name(self) -> str:
    return self.__rename

  @property
  def needPercentConvert(self) -> str:
    return self.__needPercentConvert

  def __eq__(self, __value: object) -> bool:
    if __value == self:
      return True
    if not isinstance(__value, Column):
      return False

    return self.name == __value.name and \
        self.tech_name == __value.tech_name and \
        self.needPercentConvert == __value.needPercentConvert
