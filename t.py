"""
Unfortunately, 'cmp' buit-in and 'cmp' argument in sort() were removed in Python3
The official workaround is (a > b) - (a < b) (see https://docs.python.org/3.0/whatsnew/3.0.html).
"""


def cmp(a, b):
    return (a > b) - (a < b)


def cm(s1, s2):
    c = max(len(s1), len(s2))
    return cmp(s1.ljust(c, s1[-1]), s2.ljust(c, s2[-1])) or cmp(len(s2), len(s1))


import sys
import functools
inp = sys.stdin.read()[:-1]
unsarr = list(filter(lambda x: x, inp.split('\n')))
arr = sorted(unsarr, key=functools.cmp_to_key(cm), reverse=True)
print(''.join(arr))
