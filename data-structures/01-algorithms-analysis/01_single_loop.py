# Single loop -> Time Complexity O(n)
def fun(n):
    m = 0
    i = 0
    while i < n:
        m += 1
        i += 1
    return m


print("N = 100, Number of instructions in O(n)::", fun(100))
