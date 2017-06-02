#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def duplicate_count(text):
    text = text.lower()#ignore case
    result = 0
    a = set(text)
    for i in a:
        if text.count(i) > 1:
            result += 1
    return result

print(duplicate_count("aa11"))

end = dt.datetime.now()
print(end - start)
