#!/usr/bin/env python3

NAME = "John"

if NAME == "John":
    print("Hi, John!")
elif NAME == "Mary":
    print("Hi, Mary!")
else:
    print("Hello, stranger!")

BOOL_VALUE = True
NONE_VALUE = None

if BOOL_VALUE:
    print("1: Bool value is True")

if BOOL_VALUE is True:  # instead of BOOL_VALUE == True
    print("2: Bool value is True")

if BOOL_VALUE is not False:  # instead of BOOL_VALUE == True
    print("3: Bool value is not false")

print("bool(0)", bool(0))
print("bool(1)", bool(1))
print("bool('')", bool(""))
print("bool('a')", bool("a"))

TRUE_VAL = True
FALSE_VAL = False

if TRUE_VAL and FALSE_VAL:
    print("TRUE_VAL and FALSE_VAL")
if TRUE_VAL or FALSE_VAL:
    print("TRUE_VAL or FALSE_VAL")
if TRUE_VAL and (not FALSE_VAL):
    print("TRUE_VAL and not FALSE_VAL")

print("True == False:", True == False)
print("True != False:", True != False)

##### WALRUS OPERATOR
if (dozen := 7 + 5) == 12:
    print("Dozen 1 (12): ", dozen)
print("Dozen 2: ", dozen)

if dozen2 := 7 + 5 == 12:
    print("Dozen 1 (True): ", dozen2)
print("Dozen 2: ", dozen2)
