# Greatest Common Divisor (GCD) using Euclid's algorithm
# Example 1.17
def gcd(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    return gcd(n, m % n)


# Testing code.
print("Gcd is::", gcd(5, 2))
