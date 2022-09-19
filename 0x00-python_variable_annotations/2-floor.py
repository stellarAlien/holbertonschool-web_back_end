#!/usr/bin/env python3
from math import modf
"""_summary_
contains floor function
that uses math.floor() method
"""


def floor(n: float) -> int:
    '''return the integer part of a flaot'''
    return int(modf(n)[1])
