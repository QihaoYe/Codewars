#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def divisors(n):
    return [i for i in range(2, n) if not n % i] or '%d is prime' % n

end = dt.datetime.now()
print(end - start)
