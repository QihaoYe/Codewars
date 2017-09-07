#!/usr/bin/env python3
# coding: utf-8
import datetime as dt
start = dt.datetime.now()

# time out
def dbl_linear(n):
    result = [1]
    i = 0
    j = 0
    while len(result) < n + 1 or 3*result[j]+1 < result[-1]:
        result.append(2*result[i]+1)
        while 3*result[j]+1 < result[-1]:
            result.append(3*result[j]+1)
            j += 1
        result = sorted(list(set(result)))
        i += 1
    return result

N = 10000
a = dbl_linear(N)
print(a)
print(a[N])
print(len(a)-1)


end = dt.datetime.now()
print(end - start)
