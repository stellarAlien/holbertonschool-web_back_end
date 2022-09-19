#!/usr/bin/env python3
"""_summary_
insert right annotations
"""

from typing import Any, TypeVar, Union, NoReturn, Mapping
# https://stackoverflow.com/questions/58755948/what-is-the-difference-between-typevar-and-newtype

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]
                     = None) -> Union[Any, T]:
    '''safely get dct[key]'''
    if key in dct:
        return dct[key]
    else:
        return default
