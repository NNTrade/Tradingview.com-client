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

    def set_field(self, field: str) -> Filter:
        self.field = field
        return self

    def set_compare_func(self, compare_func: Filter.CompareFunc) -> Filter:
        self.compare_func = compare_func
        return self

    def set_value(self, value: any) -> Filter:
        self.value = value
        return self


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

    def set_field_idf(self, field: str) -> Sort:
        self.field = field
        return self

    def set_is_asc(self, is_asc: bool) -> Sort:
        self.is_asc = is_asc
        return self


class Range:
    def __init__(self, from_idx: int, till_idx: int) -> None:
        self.from_idx = from_idx
        self.till_idx = till_idx

    def set_from_idx(self, idx: int) -> Range:
        self.from_idx = idx
        return self

    def set_till_idx(self, idx: int) -> Range:
        self.till_idx = idx
        return self

    def to_request_dict(self) -> Dict:
        return [
            self.from_idx,
            self.till_idx
        ]

    def clone(self) -> Range:
        return Range(self.from_idx, self.till_idx)


class RequestContext:
    def __init__(self, range: Range = Range(0, 1000000000), filters: List[Filter] = None, sort: Sort = Sort("name")) -> None:
        self.range = range
        self.filters = filters if filters is not None else []
        self.sort = sort

    def clone(self) -> RequestContext:
        return RequestContext(self.range.clone(), [f.clone() for f in self.filters], self.sort.clone())

    def set_filters(self, filters: List[Filter]) -> RequestContext:
        self.filters = filters
        return self

    def add_filter(self, filter: Filter) -> RequestContext:
        self.filters.append(filter)
        return self

    def set_sort(self, sort: Sort) -> RequestContext:
        self.sort = sort
        return self

    def set_range(self, range: Range) -> RequestContext:
        self.range = range
        return self
