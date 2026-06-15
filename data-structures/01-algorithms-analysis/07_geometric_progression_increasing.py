# Nested loops / Geometric progression (increasing) -> Time Complexity O(n)
def fun(n):
    m = 0
    i = 1
    while i <= n:
        j = 0
        while j <= i:
            m += 1
            j += 1
        i *= 2
    return m


print("N = 100, Number of instructions in O(n)::", fun(100))
