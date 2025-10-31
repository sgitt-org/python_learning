#!/usr/bin/env python3

name = "Bob"  # pylint: disable=invalid-name
name2 = "Alice"


def greet_user(user_name):
    print(f"Hello {user_name}")


greet_user(name.upper())
greet_user(name2)
print("Hello World")

if name == "Bob":
    print("Welcome back, Bob!")
else:
    print("Hello, stranger!")
