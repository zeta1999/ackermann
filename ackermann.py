#! /usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

def ackermann_1(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann_1(m - 1, 1)
    else:
        return ackermann_1(m - 1, ackermann_1(m, n - 1))

def ackermann_2(m, n):
    while m >= 4:
        if n == 0:
            n = 1
        else:
            n = ackermann_2(m, n - 1)
        m -= 1
    if m == 3:
        return (1 << n + 3) - 3
    elif m == 2:
        return (n << 1) + 3
    elif m == 1:
        return n + 2
    else:
        return n + 1

if __name__ == "__main__":
    # Point of entry in execution mode
    m, n = int(sys.argv[1]), int(sys.argv[2])
    print(ackermann_1(m, n))
    print(ackermann_2(m, n))
