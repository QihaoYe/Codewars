#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextlib
import datetime as dt


@contextlib.contextmanager
def timer():
    start = dt.datetime.now()
    yield
    end = dt.datetime.now()
    print(end - start)


with timer():
    pass
