#!/usr/bin/env python3
# coding: utf-8

import datetime as dt

start = dt.datetime.now()

def index(array, n):
    try:
        return array[n]**n
    except:
        return -1

print(index([1,10,100,1000],3))
print(index([1,10,100,1000],4))

end = dt.datetime.now()
print(end - start)
