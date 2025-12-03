#!/usr/bin/env python3
import math
from textwrap import dedent

STRING_1 = "Hi!"
STRING_2 = 'Hi!'
STRING_3 = """\
It's a text
  Another line"""
STRING_4 = '''\
Some text
  Text
Text'''
STRING_5 = '''
              Some text
                Text
              Text'''

print(STRING_1)
print(STRING_2)
print(STRING_3)
print(STRING_4)

print(STRING_5)
print(dedent(STRING_5))

print("Hello " "World" "!")  # String concatenation

#### Raw strings
print("Normal string with \n\t escape signs")
print(r"Raw \n\string")

##### Formatted strings
COUNT = 12
print("There are " + str(COUNT) + " eggs")
print(f"There are {COUNT} eggs")
print(f"{2*2=}")  # 2*2=4
print(f"{math.pi*2=}")  # math.pi*2=6.283185307179586
print(f"{{2*2}}")  # {2*2} - output { literal
print(f"{{{2 * 2}}}")  # {4}
