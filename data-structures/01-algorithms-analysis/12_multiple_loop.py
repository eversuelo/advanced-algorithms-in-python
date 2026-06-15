# Multiple loop -> Time Complexity O(n)
# j is NOT reset, so the inner loop runs n times in total across all iterations.
def fun(n):
    m = 0
    i = 0
    j = 0
    while i < n:
        while j < n:
            m += 1
            j += 1
        i += 1
    return m


print("N = 100, Number of instructions in O(n)::", fun(100))
