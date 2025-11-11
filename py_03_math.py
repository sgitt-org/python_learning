#!/usr/bin/env python3
import math
from decimal import Decimal
from fractions import Fraction

# Python has no limit to how long an integer value can be. The only constraint is the amount of memory your system has
INT = 100_000_000_000
FLOAT = 1.0

INVALID_FLOAT = float("nan")
print(INVALID_FLOAT)

INFINITY_FLOAT = float("inf")
print(INFINITY_FLOAT)

INFINITY_MATH = math.inf
print("INF: " + str(INFINITY_FLOAT == INFINITY_MATH))

INFINITY_FLOAT_MATH = math.inf
print(INFINITY_FLOAT_MATH)

MINUS_INFINITY_FLOAT = float("-inf")
print(MINUS_INFINITY_FLOAT)

################ Fractin and Decimal
third_fraction = Fraction(1, 3)
print(third_fraction)
print(type(third_fraction))

third_fixed = Decimal("0.333")
print(third_fixed)

third_float = 1 / 3
print(third_float)

third_float = float(third_fraction)
print(third_float)

third_int = int(third_fraction)
print(third_int)

third_str = str(third_fraction)
print(third_str)

########### The java.math.BigDecimal in Java's equivalent is decimal.Decimal in Python
DEC_0_3 = Decimal("0.1") + Decimal("0.2")
print(DEC_0_3)

FLOAT_0_3 = 0.1 + 0.2
print(FLOAT_0_3)

############ Math operators
print(abs(-42))
print(abs(680 // 16))
print(abs(680 % 16))
print(abs(2 ** 2))
print("-----------")
print(math.sqrt(100))
print(math.log(100))
print(math.log10(100))
print(math.log2(100))
print(math.pow(2, 10))
print(math.factorial(5))
print(math.gcd(12, 18))
print(math.isqrt(100))
