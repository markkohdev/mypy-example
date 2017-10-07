"""
This file contains examples of how to use MyPy to perform static type checking.
This code will be passing in the master branch.  Look at the bad-stuff branch/PR to see failures.
"""
from typing import Any, Optional, Iterator


class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def rename(self, new: str) -> None:
        self.name = new

    def describe(self) -> str:
        return 'My name is {} and I am {} years old.'.format(self.name, self.age)


p = Person('Mark', 24)
print(p.describe())


# FAIL CASES
print(p.decribe())


def func_with_optional(opt: Optional[str] = None) -> Optional[str]:
    if opt is not None:
        return 'Func was passed a value: ' + opt
    return None


# We can call func_with_optional
print(func_with_optional('banana'))
# Or without one
print(func_with_optional())


# FAIL CASES
func_with_optional(1)
func_with_optional(x)


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


fibs = fib(21)


# FAIL CASES
some_value = some_func(-10)  # type: str
fib(some_value)
other_value: str = some_func(-10)
fib(other_value)

def foo(a: str) -> str:
    # return '(' + a.strip() + ')'
    # FAIL CASES
    return '(' + a.split() + ')'
