#!/usr/bin/env python3

name = "Bob"
name2 = "Alice"


def greetUser(userName):
    print(f"Hello {userName}")


greetUser(name.upper())
greetUser(name2)
print("Hello World")

if name == "Bob":
    print("Welcome back, Bob!")
else:
    print("Hello, stranger!")
