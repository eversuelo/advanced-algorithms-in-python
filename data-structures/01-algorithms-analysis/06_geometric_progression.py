# Nested loops / Geometric progression -> Time Complexity O(n)
def fun(n):
    m = 0
    i = n
    while i > 0:
        j = 0
        while j < i:
            m += 1
            j += 1
        i //= 2
    return m


print("N = 100, Number of instructions in O(n)::", fun(100))
