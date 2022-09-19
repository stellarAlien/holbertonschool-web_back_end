#!/usr/bin/env python3
"""_summary_
    insert right annotations
"""
from typing import Iterable, Sequence

def element_length(lst: Iterable[str]) -> tuple(Sequence, int):
    return [(i, len(i)) for i in lst]