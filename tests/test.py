# -*- coding: utf-8 -*-


def range_number(n):
    for x in range(0, n):
        yield x

print range_number(10)
