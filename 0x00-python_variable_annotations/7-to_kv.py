#!/usr/bin/env python3
'''Task 7's module.
'''
from typing import Tuple, Union


def to_kv(k: str, v: int | float) -> Tuple[str, float]:
    '''Converts a key and its value to a tuple and a square
    '''
    return (k , float(v ** 2))
