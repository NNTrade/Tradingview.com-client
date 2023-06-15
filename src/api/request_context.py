from __future__ import annotations
from enum import Enum
from typing import Dict, List


class Filter:
    class CompareFunc(Enum):
        eq = "equal"
        notEmpty = "nempty"
        gt = "greater"
        ls = "less"

    def __init__(self, field: str, compare_func: Filter.CompareFunc, value: any) -> None:
        self.field = field
        self.compare_func = compare_func
        self.value = value
        pass

    def to_request_dict(self) -> Dict:
        return {
            "left": self.field,
            "operation": self.compare_func.value,
            "right": self.value
        }

    def clone(self) -> Filter:
        return Filter(self.field, self.compare_func, self.value)


class Sort:
    def __init__(self, field: str, is_asc: bool = True) -> None:
        self.field = field
        self.is_asc = is_asc

    def to_request_dict(self) -> Dict:
        return {
            "sortBy": self.field,
            "sortOrder": "asc" if self.is_asc else "desc"
        }

    def clone(self) -> Sort:
        return Sort(self.field, self.is_asc)


class Range:
    def __init__(self, from_idx: int, till_idx: int) -> None:
        self.from_idx = from_idx
        self.till_idx = till_idx

    def to_request_dict(self) -> Dict:
        return [
            self.from_idx,
            self.till_idx
        ]

    def clone(self) -> Range:
        return Range(self.from_idx, self.till_idx)


class RequestContext:
    def __init__(self, range: Range = Range(0, 1000000000), filters: List[Filter] = [], sort: Sort = Sort("name")) -> None:
        self.range = range
        self.filters = filters
        self.sort = sort

    def clone(self) -> RequestContext:
        return RequestContext(self.range.clone(), [f.clone() for f in self.filters], self.sort.clone())
