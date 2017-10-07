"""
This file contains more fancy examples of how to use MyPy to perform static type checking.
This code will be passing in the master branch.  Look at the bad-stuff branch/PR to see failures.
"""
from typing import Dict, List, Optional, Union

# This is called type Aliasing.  I don't wanna type this big type out all over the place
# so now I can just use `ComplexDictType`
# Note: It probably makes sense to turn this into a class!
MyComplexDict = Dict[str, List[Dict[str, Union[List[int], int]]]]


def complex_dict_consumer(jawn: Optional[MyComplexDict]) -> str:
    if jawn is None:
        return ''
    result: List[str] = []
    for key, value in jawn.items():
        partial_result = '{}: '.format(key)
        for sub_dict in value:
            for subkey, subvalue in sub_dict.items():
                if isinstance(subvalue, list):
                    joined = ' + '.join([str(i) for i in subvalue])
                    partial_result += '({} = {})'.format(subkey, joined)
                else:
                    partial_result += '({} = {})'.format(subkey, subvalue)
        result.append(partial_result)

    return ', '.join(result)


crazy_dict = {
    'some': [{'thing': 1, 'crazy': 2, 'is': [3, 4, 5], 'up': 6},
             {}],
    'ayeee': [],
    'blurp': [{'testing': 0}]
}

# MYPY FAILURE IF NO ANNOTATION :(
# mypy_example/fancier_examples.py:36: error: Argument 1 to "complex_dict_consumer" has incompatible type Dict[str, object]; expected "Optional[Dict[str, List[Dict[str, Union[List[int], int]]]]]"
useless_result = complex_dict_consumer(crazy_dict)
print(useless_result)


# TODO: Do some fancy examples with generics here
# http://mypy.readthedocs.io/en/stable/generics.html
