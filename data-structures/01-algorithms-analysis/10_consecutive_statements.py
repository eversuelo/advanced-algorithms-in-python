# Consecutive statements -> Time Complexity O(n^2)
def fun(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            m += 1
            j += 1
        i += 1

    i = 0
    while i < n:
        k = 0
        while k < n:
            m += 1
            k += 1
        i += 1
    return m


print("N = 100, Number of instructions in O(n^2)::", fun(100))
