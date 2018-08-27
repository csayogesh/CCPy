#!/bin/python3

import sys


def sums(n):
    return int(n * (n + 1))>>1


def do(n):
    n -= 1
    tees = sums(int(n / 3))
    fives = sums(int(n / 5))
    fifteens = sums(int(n / 15))
    return 3 * tees + 5 * fives - 15 * fifteens


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = do(n)
    print(ans)
