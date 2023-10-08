#!/usr/bin/env python3

'''
Method that determines if all boxes can be opened
'''

from typing import Any, Union, Mapping, TypeVar

T = TypeVar('T')
NoneType = TypeVar('NoneType', None, None)
R = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D) -> R:
    '''
    Returns the value
    '''
    if key in dct:
        return dct[key]
    else:
        return default