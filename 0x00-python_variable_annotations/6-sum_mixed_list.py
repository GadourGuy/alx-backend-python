#!/usr/bin/env python3
'''Task 6's module.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    ''' sums a list
    '''
    return float(sum(mxd_lst))
