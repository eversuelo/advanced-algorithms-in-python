# Recursive Function

**Recursion:** A recursive function is a function that calls itself, directly or indirectly.

A recursive method consists of two parts: **Termination Condition** and **Body** (which includes recursive expansion).

1. **Termination Condition:** A recursive method always contains one or more terminating conditions. A condition in which a recursive method processes a simple case and does not call itself.
2. **Body (including recursive expansion):** The main logic of the recursive method is contained in the body of the method. It also contains the recursion expansion statement that, in turn, calls the method itself.

## Properties of a Recursive Algorithm

Three important properties of the recursive algorithm are:

1. A recursive algorithm must have a termination condition.
2. A recursive algorithm must change its state, and shift state towards the termination condition.
3. A recursive algorithm must be capable of calling itself.

> **Note:** The speed of a recursive program is slower because of stack overheads. If the same problem can be solved using an iterative solution (using loops), then we should prefer an iterative solution in place of recursion to avoid stack overhead.

> **Note:** Without termination conditions, the recursive method may run forever and consume full-stack memory.

## Factorial

```python
def factorial(i):
    if i <= 1:
        return 1
    return i * factorial(i - 1)


# Testing code.
print("Factorial:", factorial(5))
```

**Analysis:** We calculate `factorial(i)` as `i * factorial(i - 1)` recursively. Function `F(n)` calls `F(n-1)`.

```
T(n)   = T(n-1) + 1
T(n-1) = T(n-2) + 1
T(n-2) = T(n-3) + 1

T(n) = T(n-1) + 1
     = (T(n-2) + 1) + 1 = T(n-2) + 2
     = (T(n-3) + 1) + 2 = T(n-3) + 3

Similarly, for the kth term:  T(n) = T(n-k) + k

For the base case (n-k) = 1, or  n - 1 = k:
T(n) = T(1) + n - 1 = n
```

**Time Complexity is O(n).**

## Print Base 16 Integers

**Problem:** Given an integer in decimal form, print its hexadecimal form. Use recursion to solve the problem.

**Example 1.15:** Generic print to some specific base method.

```python
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
```

**Output:**

```
1F4
```

**Analysis:**

1. The base value is provided along with the number in the function parameter.
2. The remainder of the number is calculated and stored in digits.
3. If the number is greater than the base, then the number divided by the base is passed recursively as an argument to the `print()` method.
4. The number will be printed higher-ordered first, then the lower order digits.

**Time Complexity is O(n)**, where `n` is the number of digits.

## Tower of Hanoi

**Problem:** In the Tower of Hanoi, we are given three rods and N number of disks. Initially all the disks are added to the first rod (the leftmost one) such that no smaller disk is under the larger one. The objective is to transfer the entire stack of disks from the first tower to the third tower (the rightmost one), moving only one disk at a time. Moving a larger disk onto a smaller one is not allowed.

**Solution:** If we want to transfer N disks from source to destination tower. Let's consider the bottom-most disk; it is the largest disk so it cannot be placed to any other tower except the destination tower. Also, all the disks above the largest disk need to be placed in the temporary tower, then only the largest disk can be moved to the destination tower. So we move N-1 disks from source to temporary tower, then move the lowest Nth disk from source to destination. Then we will move N-1 disks from the temporary tower to the destination tower.

**Example 1.16:**

```python
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
```

**Output:**

```
The sequence of moves involved in the Tower of Hanoi are:
Move 1 disk from peg A to peg C
Move 2 disk from peg A to peg B
Move 1 disk from peg C to peg B
Move 3 disk from peg A to peg C
Move 1 disk from peg B to peg A
Move 2 disk from peg B to peg C
Move 1 disk from peg A to peg C
```

**Analysis:**

```
Recurrence Relation: T(n) = 1 + 2T(n-1)
T(n-1) = 1 + 2T(n-2)
T(n-2) = 1 + 2T(n-3)

T(n) = 1 + 2(1 + 2T(n-2))
     = 1 + 2 + 4T(n-2)
     = 1 + 2 + 4(1 + 2T(n-3))
     = 1 + 2 + 2² + 2³T(n-3)
     = 1 + 2 + 2² + ... + 2ⁿT(0)
     = (2ⁿ⁺¹ - 1)        // Geometric progression sum
```

**Time complexity will be O(2^n)**, ignoring the constants.

## Greatest Common Divisor (GCD)

**Problem:** Find the greatest common divisor of two numbers using recursion.

**Solution:** There are many ways to find the greatest common divisor (GCD). We are using Euclid's algorithm to find the GCD. Following is Euclid's algorithm:

1. If `n = 0` then `GCD(n, m) = m`, and this is a termination condition.
2. If `m = 0` then `GCD(n, m) = n`, and this is a termination condition.
3. Write `n` in the form of a quotient remainder `n = mq + r`. `q` is the quotient, and `r` is the remainder.
4. Since `GCD(n, m) = GCD(m, r)`, use the Euclidean Algorithm to find `GCD(m, r)`.

**Example 1.17:**

```python
def gcd(m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    return gcd(n, m % n)


# Testing code.
print("Gcd is::", gcd(5, 2))
```

**Output:**

```
Gcd is:: 1
```

**Time-Complexity:** `O(Max(log(m), log(n)))`. Each step the input is reduced by nearly half or more.

## Fibonacci Number

**Problem:** Given N, find the Nth number in the Fibonacci series.

**Solution:** Fibonacci numbers are calculated by adding the sum of the previous two numbers.

**Example 1.18:**

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Testing code.
print(fibonacci(10))
```

**Output:**

```
55
```

**Analysis:**

```
Recurrence Relation: T(n) = 1 + T(n-1) + T(n-2)
T(n) = 1 + 2T(n-1)        // Approximately
T(n-1) = 1 + 2T(n-2)
T(n-2) = 1 + 2T(n-3)

T(n) = 1 + 2(1 + 2T(n-2))
     = 1 + 2 + 4T(n-2)
     = 1 + 2 + 4(1 + 2T(n-3))
     = 1 + 2 + 2² + 2³T(n-3)
     = 1 + 2 + 2² + ... + 2ⁿT(0)
     = (2ⁿ⁺¹ - 1)        // Geometric progression sum
```

**Time complexity is O(2^n)**, ignoring the constants.

> **Note:** There is an inefficiency in this solution. We will look for a better solution in the coming chapters.

## Ackermann Function

Most of the time we can solve a recursive problem using loops, but not always. A primitive recursive function is a function that can be represented using loops. The **Ackermann function** is the simplest example of a well-defined total function which is computable but not primitive recursive.

The Ackermann function is defined as:

```
Ack(m, n) = n + 1                       if m = 0
          = Ack(m - 1, 1)               if m > 0 and n = 0
          = Ack(m - 1, Ack(m, n - 1))   if m > 0 and n > 0
```

Where `m` and `n` are non-negative.

**Example 1.19:**

```python
def ackermann(m, n):
    if m == 0:
        return n + 1
    if (m > 0) and (n == 0):
        return ackermann(m - 1, 1)
    if (m > 0) and (n > 0):
        return ackermann(m - 1, ackermann(m, n - 1))


# Testing code.
print(ackermann(3, 6))
```

**Output:**

```
509
```

---

> **Note:** The complexity analysis from recurrence relations (Examples 1.20–1.26) and the **Master Theorem** are covered in a separate document: [complexities-from-recurrence-relation.md](../complexities-from-recurrence-relation.md)
