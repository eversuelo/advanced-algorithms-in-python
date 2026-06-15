# Factorial -> recursive
def factorial(i):
    if i <= 1:
        return 1
    return i * factorial(i - 1)


# Testing code.
print("Factorial:", factorial(5))
