#!/usr/bin/env python3
# coding: utf-8

#&位运算符
#2->10,3->11,2%3->10(1 and 1 == 1,0 and 1 == 0)

import datetime as dt
start = dt.datetime.now()

def is_even(n):
    return not n & 1

end = dt.datetime.now()
print(end - start)
