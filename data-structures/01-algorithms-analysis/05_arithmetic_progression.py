# Arithmetic progression -> Time Complexity O(n^2)
def fun(n):
    m = 0
    i = 0
    while i < n:
        j = i
        while j > 0:
            m += 1
            j -= 1
        i += 1
    return m


print("N = 100, Number of instructions in O(n^2)::", fun(100))
