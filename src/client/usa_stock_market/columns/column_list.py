from .column import Column

base_cur_col = Column("fundamental_currency_code", "Base currency")
volume_col = Column("volume", "Volume / 1D")
price_change_col = Column("change", "Price change mult", True)
market_cap_col = Column("market_cap_basic", "Market cap")
type_col = Column("type")
description_col = Column("description")
dividend_yield_ttm = Column(
    "dividends_yield_current", "Dividend yield Mult TTM", True)
dividend_yield_fwd = Column("dividends_yield", "Dividend yield Mult FWD", True)

