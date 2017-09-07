#!/usr/bin/env python3
# coding: utf-8

import datetime as dt

start = dt.datetime.now()

def josephus(items,k,result=[],i=-1):
    if i == -1:result = []#注意传参问题
    loc = [x for x in range(len(items)) if not (x-i)%k]
    i = loc[-1] + k - len(items) if loc else i - len(items)
    for a in loc:result.append(items[a])
    return result if not items else josephus([items[a] for a in range(len(items)) if a not in loc],k,result,i)


print(josephus([1,2,3,4,5,6,7,8,9,10],1))
print(josephus([1,2,3,4,5,6,7,8,9,10],2))
print(josephus([1,2,3,4,5,6,7],3))





end = dt.datetime.now()
print(end - start)
