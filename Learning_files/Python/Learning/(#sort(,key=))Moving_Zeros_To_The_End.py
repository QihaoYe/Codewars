#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0 and x is not False)

end = dt.datetime.now()
print(end - start)
