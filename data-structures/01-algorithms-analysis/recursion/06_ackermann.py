# Ackermann function
# The simplest example of a well-defined total function which is computable
# but not primitive recursive.
#
# Ack(m, n) = n + 1                         if m = 0
#           = Ack(m - 1, 1)                 if m > 0 and n = 0
#           = Ack(m - 1, Ack(m, n - 1))     if m > 0 and n > 0
#
# Where m and n are non-negative.
# Example 1.19
def ackermann(m, n):
    if m == 0:
        return n + 1
    if (m > 0) and (n == 0):
        return ackermann(m - 1, 1)
    if (m > 0) and (n > 0):
        return ackermann(m - 1, ackermann(m, n - 1))


# Testing code.
print(ackermann(3, 6))
