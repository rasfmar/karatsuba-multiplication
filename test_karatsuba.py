#!/usr/bin/python3

from src.karatsuba import karatsuba;

def main():
    # test one digit products
    assert karatsuba(0, 1) == 0;
    assert karatsuba(1, 2) == 2;
    assert karatsuba(2, 4) == 8;
    assert karatsuba(3, 8) == 24;

    # test two digit products
    assert karatsuba(10, 20) == 200;
    assert karatsuba(11, 40) == 440;
    assert karatsuba(12, 80) == 960;

    # test four digit product
    assert karatsuba(1234, 5678) == 7006652;

    # test sixty-four digit product
    assert \
        karatsuba( \
            3141592653589793238462643383279502884197169399375105820974944592, \
            2718281828459045235360287471352662497757247093699959574966967627 \
        ) == 8539734222741967153090090158638514132503608418533065336905844490421604760710273353716300940806781479233403577102389712581823184;

if __name__ == "__main__":
    main();
    print("Passed tests");
