#!/usr/bin/env python3
"""_summary_
    returns an annotated tuple
"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''returns a tuple with str ad float'''
    return (k, v**2)
