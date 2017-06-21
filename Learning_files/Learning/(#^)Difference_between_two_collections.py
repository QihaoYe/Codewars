#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def diff(a, b):
    return sorted(set(a) ^ set(b))

# def diff(a, b):
#   return sorted(set(a).symmetric_difference(set(b)))

end = dt.datetime.now()
print(end - start)
