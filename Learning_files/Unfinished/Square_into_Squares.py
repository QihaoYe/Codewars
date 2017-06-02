#!/usr/bin/env python3
# coding: utf-8

import datetime as dt


start = dt.datetime.now()

def decompose(n):
    m = 2 * n - 1
    for i in range(int(m ** 0.5),int(n ** 0.5),-1):
        result = [n-1,i]
        p = m - i ** 2
        while p:
            result.append(int(p ** 0.5))
            p -= int(p ** 0.5) ** 2
        if len(result) == len(set(result)):
            return result[::-1]
    return None

print(decompose(44))

end = dt.datetime.now()
print(end - start)
