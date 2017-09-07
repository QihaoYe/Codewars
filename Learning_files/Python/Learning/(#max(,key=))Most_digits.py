#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))

print(find_longest([8, 500, 900]))

end = dt.datetime.now()
print(end - start)
