#!/usr/bin/env python3
"""_summary_
    insert right annotations
"""
from typing import TypeVar, Union, NoReturn


def safely_get_value(dct: dict, key:str, default: Union[TypeVar,NoReturn] = None) -> Union[TypeVar,NoReturn]:
    if key in dct:
        return dct[key]
    else:
        return default