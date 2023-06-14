from typing import Dict, List, Tuple
import json
import requests
from ..exceptions import DoesNotResponseException
from .symbol_query_types import SymbolQueryTypes


def post_scan(columns: List[str], get_top: int = 200, start_top_from: int = 0, top_order: str = "name", top_asc: bool = True, symbol_query_types: SymbolQueryTypes = None, filter: Tuple[SymbolQueryTypes, str] = None) -> Dict:

    url = "https://scanner.tradingview.com/america/scan"

    json_dict = {
        "columns": columns,
        "filter": [
            {
                "left": "name",
                "operation": "nempty"
            },
        ],
        "ignore_unknown_fields": False,
        "options": {
            "lang": "en"
        },
        "range": [
            start_top_from,
            get_top
        ],
        "sort": {
            "sortBy": top_order,
            "sortOrder": "asc" if top_asc else "desc"
        },
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

    if filter is not None:
        json_dict["filter"].append({
            "left": filter[0].value,
            "operation": "equal",
            "right": filter[1]
        })

    payload = json.dumps(json_dict)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise DoesNotResponseException()

    return json.loads(response.text)
