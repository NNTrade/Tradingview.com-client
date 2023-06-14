
import requests
import json
from ..exceptions import DoesNotResponseException
from typing import Dict


def request_data(str_url: str) -> requests.Response:

  response = requests.request("GET", str_url)
  return response


def get_payload(str_url: str) -> str:
  response = request_data(str_url)
  if response.status_code != 200:
    raise DoesNotResponseException()

  return response.text


def get_sectors_payload() -> str:
  url = "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-sector/"
  return get_payload(url)


def get_industries_payload() -> str:
  url = "https://www.tradingview.com/markets/stocks-usa/sectorandindustry-industry/"
  return get_payload(url)


def get_industry_json() -> Dict:

  url = "https://scanner.tradingview.com/america/scan"

  payload = json.dumps({
      "columns": [
          "description",
          "market",
          "market_cap_basic",
          "type",
          "typespecs",
          "fundamental_currency_code",
          "dividends_yield",
          "change",
          "volume",
          "sector",
          "basic_elements"
      ],
      "filter": [
          {
              "left": "description",
              "operation": "nempty"
          }
      ],
      "ignore_unknown_fields": False,
      "options": {
          "lang": "en"
      },
      "range": [
          0,
          200
      ],
      "sort": {
          "sortBy": "description",
          "sortOrder": "asc"
      },
      "symbols": {
          "query": {
              "types": [
                  "industry"
              ]
          },
          "tickers": []
      },
      "markets": [
          "america"
      ]
  })

  headers = {
      'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  if response.status_code != 200:
    raise DoesNotResponseException()

  return json.loads(response.text)
