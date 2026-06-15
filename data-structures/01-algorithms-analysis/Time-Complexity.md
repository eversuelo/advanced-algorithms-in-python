# Complexities from Recurrence Relation

## Table of Contents

- [Example 1.20](#example-120)
- [Example 1.21](#example-121)
- [Example 1.22](#example-122)
- [Recurrence Relation Summary](#recurrence-relation-summary)
- [Example 1.23](#example-123)
- [Example 1.24](#example-124)
- [Example 1.25](#example-125)
- [Example 1.26](#example-126)
- [Master Theorem](#master-theorem)

---

## Example 1.20

Find complexity of the function with the following recurrence relation.

```
T(n) = 1            if n = 0
     = T(n-1) + 1   if n > 0
```

**Solution:**

```
T(n) = T(n-1) + 1
T(n-1) = T(n-2) + 1
T(n-2) = T(n-3) + 1

T(n) = (T(n-2) + 1) + 1 = T(n-2) + 2
     = (T(n-3) + 1) + 2 = T(n-3) + 3
T(n) = T(n-k) + k

base case when T(0) = 1, n - k = 0 => n = k
T(n) = T(0) + n = 1 + n
```

**Time Complexity is O(n).**

## Example 1.21

Find complexity of the function with the following recurrence relation.

```
T(n) = 1            if n = 0
     = T(n-1) + n   if n > 0
```

**Solution:**

```
T(n) = T(n-1) + n
T(n-1) = T(n-2) + n
T(n-2) = T(n-3) + n

T(n) = (T(n-2) + n) + n = T(n-2) + 2n
     = (T(n-3) + n) + 2n = T(n-3) + 3n
T(n) = T(n-k) + kn

base case when T(0) = 1, n - k = 0 => n = k
T(n) = T(0) + n*n = 1 + n²
```

**Time Complexity is O(n^2).**

## Example 1.22

Find complexity of the function with the following recurrence relation.

```
T(n) = 1                 if n = 0
     = T(n-1) + log(n)   if n > 0
```

**Solution:**

```
T(n) = T(n-1) + log(n)
T(n-1) = T(n-2) + log(n)   // for simplicity make log(n-1) as log(n)
T(n-2) = T(n-3) + log(n)

T(n) = (T(n-2) + log(n)) + log(n) = T(n-2) + 2log(n)
     = (T(n-3) + log(n)) + 2log(n) = T(n-3) + 3log(n)
T(n) = T(n-k) + k*log(n)

base case when T(0) = 1, n - k = 0 => n = k
T(n) = T(0) + n*log(n) = 1 + n*log(n)
```

**Time Complexity is O(n.log(n)).**

## Recurrence Relation Summary

| Recurrence Relation | Time-Complexity |
|---------------------|-----------------|
| T(n) = T(n-1) + 1 | O(n) |
| T(n) = T(n-1) + n | O(n²) |
| T(n) = T(n-1) + log(n) | O(n·log(n)) |
| T(n) = T(n-c) + 1, `c` is a constant | O(n), complexity is not changed by `c`. |
| T(n) = T(n-c) + b, `c` constant & `b` a polynomial | O(n*b), generalised above 4 cases. |

## Example 1.23

Find complexity of the function with the following recurrence relation.

```
T(n) = 1            if n = 1
     = T(n/2) + n   if n > 1
```

**Solution:**

```
T(n) = T(n/2) + n
T(n/2) = T(n/2²) + (n/2)     // substituting n as n/2
T(n/2²) = T(n/2³) + (n/2²)   // substituting n as n/2²

T(n) = (T(n/2²) + (n/2)) + n = T(n/2²) + n/2 + n
     = (T(n/2³) + (n/2²)) + n/2 + n = T(n/2³) + n/2² + n/2 + n
T(n) = T(n/2^k) + n/2^(k-1) + ... + n/2² + n/2 + n

base case when n = 2^k,
T(n) = T(1) + n/2^(k-1) + ... + n/2² + n/2 + n
T(n) = T(1) + n * (1/2^(k-1) + ... + 1/2² + 1/2 + 1)
T(n) = 1 + n*2
```

**Time Complexity is O(n).**

## Example 1.24

Find complexity of the function with the following recurrence relation.

```
T(n) = 1              if n = 1
     = 2*T(n/2) + n   if n > 1
```

**Solution:**

```
T(n) = 2 T(n/2) + n
T(n/2) = 2 T(n/2²) + (n/2)     // substituting n as n/2
T(n/2²) = 2 T(n/2³) + (n/2²)   // substituting n as n/2²

T(n) = 2(2 T(n/2²) + (n/2)) + n = 2² T(n/2²) + 2n
T(n) = 2²(2 T(n/2³) + (n/2²)) + 2n = 2³ T(n/2³) + 3n
T(n) = 2^k * T(n/2^k) + kn

base case when n = 2^k, k = log(n)
T(n) = n*T(1) + k*n
T(n) = n + k*n = n + n*log(n)
```

**Time Complexity is O(n.log(n)).**

## Example 1.25

Find complexity of the function with the following recurrence relation.

```
T(n) = 1              if n = 0
     = 2*T(n-1) + 1   if n > 0
```

**Solution:**

```
T(n) = 2 T(n-1) + 1
T(n-1) = 2 T(n-2) + 1
T(n-2) = 2 T(n-3) + 1

T(n) = 2(2 T(n-2) + 1) + 1 = 2² T(n-2) + 2 + 1
     = 2²(2 T(n-3) + 1) + 2 + 1 = 2³ T(n-3) + 2² + 2 + 1
T(n) = 2^k T(n-k) + 2^(k-1) + ... + 2² + 2 + 1

base case when T(0) = 1, n - k = 0 => n = k
T(n) = 2^n T(0) + 2^(n-1) + ... + 2² + 2 + 1
     = 2^n + 2^(n-1) + ... + 2² + 2 + 1
     = 2^(n+1) - 1     // GP
```

**Time Complexity is O(2^n).**

## Example 1.26

Find complexity of the function with the following recurrence relation.

```
T(n) = 1               if n ≤ 2
     = T(√n) + 1       if n > 2
```

**Solution:**

```
T(n) = T(n^(1/2)) + 1
T(n^(1/2)) = T(n^(1/4)) + 1
T(n^(1/4)) = T(n^(1/8)) + 1

T(n) = T(n^(1/2)) + 1 = (T(n^(1/4)) + 1) + 1 = T(n^(1/4)) + 2
     = (T(n^(1/8)) + 1) + 2 = T(n^(1/8)) + 3
T(n) = T(n^(1/2^k)) + k

for base case n^(1/2^k) = 2
(1/2^k) * log(n) = log 2 = 1     // taking log
log(n) = 2^k
log(log(n)) = k*log(2) = k       // taking log again
```

**Time Complexity is O(log(log(n))).**

## Master Theorem

The master theorem solves recurrence relations of the form:

```
T(n) = a*T(n/b) + f(n),   where a ≥ 1 and b > 1
```

In this relation:

- `n` is the size of the input.
- `a` is the number of sub-problems in the recursion.
- `n/b` is the size of each sub-problem.
- `f(n)` is the cost of the division of the problem into sub-problems and merging the individual solutions of the sub-problems into the solution.

It is possible to determine an asymptotic tight bound in these three cases:

- **Case 1:** When `f(n) = O(n^(log_b(a) - ε))` and constant `ε > 1`, then the final time complexity is
  `T(n) = O(n^(log_b(a)))`.
- **Case 2:** When `f(n) = Θ(n^(log_b(a)) · log^k(n))` and constant `k ≥ 0`, then the final time complexity is
  `T(n) = Θ(n^(log_b(a)) · log^(k+1)(n))`.
- **Case 3:** When `f(n) = Ω(n^(log_b(a) + ε))` and constant `ε > 1`, then the final time complexity is
  `T(n) = Θ(f(n))`.
