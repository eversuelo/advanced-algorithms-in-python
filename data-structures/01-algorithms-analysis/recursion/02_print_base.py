# Print Base 16 Integers
# Problem: Given an integer in decimal form, print its hexadecimal form.
# Use recursion to solve the problem.
# Example 1.15: Generic print to some specific base method.
def print_int2(number, base):
    conversion = "0123456789ABCDEF"
    digit = number % base
    number = number // base
    temp = ""
    if number != 0:
        temp += print_int2(number, base)
    temp += conversion[digit]
    return temp


# Testing code.
print(print_int2(500, 16))
