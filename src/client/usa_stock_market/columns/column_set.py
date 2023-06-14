from . import column_list as colList

stock_columns = [
    colList.Column("name"),
    colList.description_col,
    colList.type_col,
    colList.Column("close"),
    colList.Column("pricescale", "Decimal Len"),
    colList.Column("currency", "Currency"),
    colList.price_change_col,
    colList.Column("change_abs", "Change in Cur / 1D"),
    colList.volume_col,
    colList.Column("Value.Traded", "Volume * Price / 1D"),
    colList.market_cap_col,
    colList.base_cur_col,
    colList.Column("price_earnings_ttm", "Price/EarningPerShare"),
    colList.Column("earnings_per_share_basic_ttm", "BasicEarningPerShare"),
    colList.Column("dps_common_stock_prim_issue_fy", "Dividend/Share"),
    colList.dividend_yield_ttm,
    colList.dividenc_yield_fwd
]
_area_columns = [colList.description_col,
                 colList.Column("market", "Market"),
                 colList.market_cap_col,
                 colList.type_col,
                 colList.base_cur_col,
                 colList.dividenc_yield_fwd,
                 colList.price_change_col,
                 colList.volume_col,
                 colList.Column("basic_elements", "Stocks")]

industry_columns = _area_columns + [
    colList.Column("sector", "Sector")
]

sector_columns = _area_columns + [
    colList.Column("elements", "Industries")
]
