#!/usr/bin/env python3
# coding: utf-8

import datetime as dt
start = dt.datetime.now()

def namelist(names):
  return ", ".join([name["name"] for name in names])[::-1].replace(",", "& ",1)[::-1]

end = dt.datetime.now()
print(end - start)
