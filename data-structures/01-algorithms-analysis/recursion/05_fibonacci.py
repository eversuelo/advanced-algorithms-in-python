# Fibonacci number
# Problem: Given N, find the Nth number in the Fibonacci series.
# Example 1.18
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Testing code.
print(fibonacci(10))
