#!/usr/bin/env python3
from math import modf
"""_summary_
    contains floor function
    that uses math.floor() method
"""


def floor(n: float) -> float:
    return modf(n)[1]
