from typing import Dict, List, Tuple
import json
import requests
from ..exceptions import DoesNotResponseException
from .symbol_query_types import SymbolQueryTypes
from .request_context import Filter, Sort, RequestContext


def post_scan(columns: List[str],
              context: RequestContext = RequestContext(),
              symbol_query_types: SymbolQueryTypes = None) -> Dict:

    url = "https://scanner.tradingview.com/america/scan"

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
            "america"
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

    payload = json.dumps(json_dict)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise DoesNotResponseException()

    return json.loads(response.text)
