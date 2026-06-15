# Tower of Hanoi
# Example 1.16
def tower_of_hanoi(num, src, dst, temp):
    if num < 1:
        return
    tower_of_hanoi(num - 1, src, temp, dst)
    print("Move", num, "disk from peg", src, "to peg", dst)
    tower_of_hanoi(num - 1, temp, dst, src)


def toh(num):
    print("The sequence of moves involved in the Tower of Hanoi are:")
    tower_of_hanoi(num, 'A', 'C', 'B')


# Testing code.
toh(3)
