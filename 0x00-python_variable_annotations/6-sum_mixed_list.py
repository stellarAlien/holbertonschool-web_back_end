#!/usr/bin/env python3
"""_summary_
    sums a list of ints and floats
"""
from typing import Union
from math import fsum
def sum_mixed_list(mxd_lst: (Union[int, float])) -> float:
    return fsum(mxd_lst)