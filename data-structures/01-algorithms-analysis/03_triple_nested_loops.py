# Triple nested loops -> Time Complexity O(n^3)
def fun(n):
    m = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            k = 0
            while k < n:
                m += 1
                k += 1
            j += 1
        i += 1
    return m


print("N = 100, Number of instructions in O(n^3)::", fun(100))
