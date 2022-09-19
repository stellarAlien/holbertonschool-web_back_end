#!/usr/bin/env python
"""_summary_
    returns a function that multiplies a float by multiplier.
"""
from operator import mul
from typing import Callable
def f(multiplier: float) -> float:
    x = multiplier
    return( x * multiplier)
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return f(multiplier)
