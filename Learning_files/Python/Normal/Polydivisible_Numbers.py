#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2018/01/06'


CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
def change_base(n, b):
    if n is 0:
        return ''
    x, y = divmod(n, b)
    return change_base(x, b) + CHARS[y]


def change_10base(s, b):
    result = 0
    for i in range(len(s) - 1, -1, -1):
        result += CHARS.index(s[i]) * (b ** (len(s) - i - 1))
    return result


def is_polydivisible(s, b):

    for i in range(1, len(s) + 1):
        if change_10base(s[:i], b) % i is not 0:
            return False
    return True


def get_polydivisible(n, b):
    count = 1
    num = 0
    num_base = '0'
    while count < n:
        num += 1
        num_base = change_base(num, b)
        if is_polydivisible(num_base, b):
            count += 1
    return num_base
