# What is this?
This is a Python3 script that utilizes the Karatsuba algorithm to effectively compute the product of large integers. It has a preference for integers of the same length.

# How do I use this?
Tests can be executed using:
```shell
python3 test_karatsuba.py
```

You can import and use this function as follows:
```python
from src.karatsuba import karatsuba;
print(karatsuba(24, 16)); # 384
print(karatsuba(12345678, 10111213)); # 124829779887414
```

# Why did I make this?
It was a programming assignment part of the algorithms specialization provided by Stanford University through Coursera. I also wanted to see if I could.
