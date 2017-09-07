#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

# cmp(x, y)
# 比较两个对象x和y，如果x < y ,返回负数；x == y, 返回0；x > y,返回正数
# 该函数只有在python2中可用，而且在python2所有版本中都可用
# 但是在python3中该函数已经被删减掉

# def no_ifs_no_buts(a, b):
#     return '%s is %s %s' % (a, ['equal to', 'greater than', 'smaller than'][cmp(a, b)], b)

def no_ifs_no_buts(a, b):
    return {
        a == b: str(a) + " is equal to " + str(b),
        a < b: str(a) + " is smaller than " + str(b),
        a > b: str(a) + " is greater than " + str(b),
    }[True]

print(no_ifs_no_buts(3,5))

end = dt.datetime.now()
print(end - start)
