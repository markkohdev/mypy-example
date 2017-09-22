# -*- coding: utf-8 -*-
# Copyright © 2017 Spotify AB


def untyped_func(untyped_var):
    print(untyped_var)


def add_to_banana(to_add: str) -> str:
    return 'Banana' + to_add


should_fail = add_to_banana(5)
