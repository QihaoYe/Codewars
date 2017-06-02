#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

# #python2
# def string_clean(s):
#     return s.translate(None,'0123456789')

def string_clean(s):
    t = s.maketrans('','','0123456789')#(a,b,c),where (a->b)&(c->None)
    return s.translate(t)

print(string_clean('1hjg23g13h42k'))

end = dt.datetime.now()
print(end - start)
