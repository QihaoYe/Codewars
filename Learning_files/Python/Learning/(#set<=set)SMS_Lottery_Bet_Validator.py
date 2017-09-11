#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextlib
import datetime as dt


@contextlib.contextmanager
def timer():
    start = dt.datetime.now()
    yield
    end = dt.datetime.now()
    print(end - start)


with timer():
    def validate_bet(game, text):
        n, m = game
        if set(text) <= set('1234567890, '):
            nums = sorted(map(int, text.replace(',', ' ').split()))
            if len(nums) == len(set(nums)) == n and 1 <= min(nums) < max(nums) <= m:
                return nums

    print(validate_bet([5, 90], "5 , 3, 1  4,2"))
