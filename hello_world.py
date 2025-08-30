name = "Bob"
name2 = "Alice"


def greetUser(name):
    print(f"Hello {name}")


greetUser(name.upper())
greetUser(name2)
print("Hello World")

if name == "Bob":
    print("Welcome back, Bob!")
else:
    print("Hello, stranger!")
