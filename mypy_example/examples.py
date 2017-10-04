# -*- coding: utf-8 -*-
# Copyright © 2017 Spotify AB
"""
This file will contain examples of how to use MyPy to perform static type checking.  It's pretty
neat, in my opinion.
"""
from typing import Any, Optional, Iterator
import random


def func_with_optional(opt: Optional[str] = None) -> Optional[str]:
    if opt is not None:
        return 'Func was passed a value: ' + opt
    return None


def add_to_banana(to_add: str) -> str:
    return 'Banana' + to_add


def some_func(num: int) -> Any:
    if num >= 0:
        return 1
    else:
        return 'potato'


def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

# This will fail:
# some_value = some_func(-10)  # type: str
# fib(some_value)

# We can call func_with_optional
print(func_with_optional('banana'))
# Or without one
print(func_with_optional())
