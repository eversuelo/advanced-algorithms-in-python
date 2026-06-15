# Double the iteration variable -> Time Complexity O(log(n))
def fun(n):
    m = 0
    i = 1
    while i < n:
        m += 1
        i = i * 2
    return m


print("N = 100, Number of instructions in O(log(n))::", fun(100))
