#!/usr/bin/python3

from math import ceil;

def karatsuba(x, y):
    x = int(x);
    y = int(y);
    n = max(len(str(x)), len(str(y)));

    if n == 1:
        return x * y;

    a = x // (10 ** ceil(n / 2));
    b = x % (10 ** ceil(n / 2));
    c = y // (10 ** ceil(n / 2));
    d = y % (10 ** ceil(n / 2));

    ac = karatsuba(a, c);
    bd = karatsuba(b, d);
    adbc = karatsuba(a + b, c + d) - ac - bd;

    return (ac * 10 ** n) + (adbc * 10 ** ceil(n / 2)) + bd;
