from typing import Dict, List, Tuple
import json
import requests
from ..exceptions import DoesNotResponseException
from .symbol_query_types import SymbolQueryTypes
from .request_context import Filter, Sort, RequestContext
from logging import getLogger


def post_scan(columns: List[str],
              context: RequestContext = RequestContext(),
              symbol_query_types: SymbolQueryTypes = None,
              filters: List[Filter] = None) -> Dict:
    post_logger = getLogger("post_scan")

    url = f"https://scanner.tradingview.com/{context.market.value}/scan"

    json_dict = {
        "columns": columns,
        "filter": [
            {
                "left": "name",
                "operation": "nempty"
            },
            {
                "left": "typespecs",
                "operation": "has_none_of",
                "right": "preferred"
            }
        ],
        "ignore_unknown_fields": False,
        "options": {
            "lang": "en"
        },
        "range": context.range.to_request_dict(),
        "sort": context.sort.to_request_dict(),
        "markets": [
            context.market.value
        ]
    }

    if symbol_query_types is not None:
        json_dict["symbols"] = {
            "query": {
                "types": [
                    symbol_query_types.value
                ]
            },
            "tickers": []
        }

    for filter in context.filters:
        json_dict["filter"].append(filter.to_request_dict())

    if filters is not None:
        for filter in filters:
            json_dict["filter"].append(filter.to_request_dict())

    post_logger.debug("json_dict: %s", json_dict)
    payload = json.dumps(json_dict)

    headers = {
        'Content-Type': 'application/json'
    }

    post_logger.debug("Request payload: %s", payload)
    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise DoesNotResponseException(response.text)

    return json.loads(response.text)
