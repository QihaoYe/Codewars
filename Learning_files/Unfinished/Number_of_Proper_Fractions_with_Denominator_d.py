#!/usr/bin/env python2
# coding: utf-8

# Try 1
# from fractions import Fraction

import datetime as dt
start = dt.datetime.now()

# def proper_fractions(n):
#     Try 1
#     return sum(0 if int(str(Fraction(i,n)).split('/')[1])-n else 1 for i in xrange(1,n))
#     !!!Time out!!!

def proper_fractions(n):
    fra = range(1,n)
    div = []
    if n % 2 == 0:
        fra = [x for x in fra if x % 2]
        div.append(2)
    for i in xrange(3,int(n/2)+1,2):
        if n % i == 0:
            flag = 0
            for j in div:
                if i % j == 0:
                    flag = 1
                    break
            if flag:continue
            div.append(i)
            fra = [x for x in fra if x % i]
    return len(fra)

print(proper_fractions(3489150))
end = dt.datetime.now()
print(end - start)
