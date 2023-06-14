# Tradingview.comm client
- [Data model](./doc/Datamodel.md)

## Install
NNTrade.datasource.tradingview @ git+ssh://git@github.com/NNTrade/Tradingview.com-client.git#egg=NNTrade.datasource.tradingview

## Using
### Get data
```python
from NNTrade.datasource.tradingview.client.usa_stock_market import get_industries, get_sectors, get_stocks, get_stock_by, get_stock_by_series, get_sector_stocks, get_industry_stocks

get_sectors()

get_industries()

get_stock()

```

### Get columns
```pythom
from NNTrade.datasource.tradingview.client.usa_stock_market.columns.column_list import * as cols
```
