# Chapter 1: Algorithms Analysis

## Table of Contents

- [Introduction](#introduction)
  - [Properties of an Algorithm](#properties-of-an-algorithm)
  - [Complexity of an Algorithm](#complexity-of-an-algorithm)
- [Asymptotic Analysis or Asymptotic Notations](#asymptotic-analysis-or-asymptotic-notations)
- [Big-O Notation](#big-o-notation)
- [Omega-Ω Notation](#omega-Ω-notation)
- [Theta-Θ Notation](#theta-Θ-notation)
- [Complexity Analysis of Algorithms](#complexity-analysis-of-algorithms)
- [Growth of Functions](#growth-of-functions)
  - [Constant Time, O(1)](#constant-time-o1)
  - [Linear Time, O(n)](#linear-time-on)
  - [Logarithmic Time, O(log(n))](#logarithmic-time-ologn)
  - [n·log(n) Time, O(n·log(n))](#nlogn-time-onlogn)
  - [Quadratic Time, O(n²)](#quadratic-time-on²)
  - [Exponential Time, O(2ⁿ)](#exponential-time-o2ⁿ)
  - [Factorial Time, O(n!)](#factorial-time-on)
  - [Common Time Complexities](#common-time-complexities)
  - [Growth Rate Comparison](#growth-rate-comparison)
- [Deriving an Algorithm's Runtime Function](#deriving-an-algorithms-runtime-function)
  - [Constants](#constants)
  - [Loops](#loops)
  - [Nested Loops](#nested-loops)
  - [Consecutive Statements](#consecutive-statements)
  - [If-Else Statement](#if-else-statement)
  - [Logarithmic Statement](#logarithmic-statement)
- [Recursive Function](#recursive-function)

---

## Introduction

An **Algorithm** is a finite set of unambiguous steps or instructions to solve a given problem. Knowledge of algorithms helps us to get desired results faster by applying the appropriate algorithm. We learn by experience. With experience, it becomes easy to solve new problems. By looking into various problem-solving algorithms or techniques, we begin to develop a pattern that will help us in solving similar problems.

### Properties of an Algorithm

The properties of an algorithm are:

1. It takes zero or more inputs.
2. It should produce one or more output.
3. It should be **Deterministic**. It produces the same output if the same input is provided again.
4. It should be **Correct**. It should be correct and able to process all the given inputs and provide the correct output.
5. It should **Terminate** in a finite time.
6. It should be **Efficient**. The algorithm should be efficient in solving problems.

### Complexity of an Algorithm

**Complexity** of an algorithm is the amount of Time or Space required by the algorithm to process the input and produce the output.

There are two types of complexity:

1. **Time-Complexity**: how much time is required by an algorithm to produce output for an input of size `n`. Time-Complexity is represented by the function `T(n)` — time required versus the input size `n`.
2. **Space-Complexity**: how much RAM or memory that an algorithm is going to consume to produce output for an input of size `n`. Space-Complexity is represented by the function `S(n)` — memory used versus the input size `n`.

---

## Asymptotic Analysis or Asymptotic Notations

Calculating the running time of any algorithm in mathematical units of computation is known as **Asymptotic Analysis**. The efficiency of algorithms is calculated using asymptotic analysis, independent of the given data set or programming language.

In most cases, we are interested in the **order of growth** of the algorithm instead of the exact time required for running an algorithm. This time is also known as **Asymptotic Running Time**.

---

## Big-O Notation

**Definition:** "*f(n)* is big-O of *g(n)*" or *f(n) = O(g(n))*, if there are two positive constants `c` and `n₁` such that:

```
f(n) ≤ c · g(n)   for all n ≥ n₁
```

In other words, `c · g(n)` is an **upper bound** for `f(n)` for all `n ≥ n₀`. The function `f(n)` growth is slower than `c · g(n)`. For a sufficiently large value of input `n`, the `c · g(n)` will always be greater than `f(n)`.

**Example:** `n² + n = O(n²)`

---

## Omega-Ω Notation

**Definition:** "*f(n)* is omega of *g(n)*" or *f(n) = Ω(g(n))*, if there are two positive constants `c` and `n₁` such that:

```
c · g(n) ≤ f(n)   for all n ≥ n₁
```

In other words, `c · g(n)` is the **lower bound** for `f(n)`. The function `f(n)` growth is faster than `c · g(n)`.

**Example:** Find the relationship of `f(n) = nᶜ` and `g(n) = cⁿ`:

```
f(n) = Ω(g(n))
```

---

## Theta-Θ Notation

**Definition:** "*f(n)* is theta of *g(n)*" or *f(n) = Θ(g(n))*, if there are three positive constants `c₁`, `c₂` and `n₁` such that:

```
c₁ · g(n) ≤ f(n) ≤ c₂ · g(n)   for all n ≥ n₁
```

The function `g(n)` is an **asymptotically tight bound** on `f(n)`. The function `f(n)` grows at the same rate as `g(n)`.

**Examples:**

```
n³ + n² + n = Θ(n³)
n² + n      = Θ(n²)
```

**Example:** Find the relationship of `f(n) = 2n² + n` and `g(n) = n²`:

```
f(n) = O(g(n))
f(n) = Θ(g(n))
f(n) = Ω(g(n))
```

---

## Complexity Analysis of Algorithms

The complexity of an algorithm is analysed in three categories:

- **Worst-Case Complexity:** The worst-case complexity represents the maximum number of steps required to execute an algorithm. It provides us with the **upper bound** of an algorithm. Usually, we use this complexity to judge algorithm performance.
- **Best-Case Complexity:** The best-case complexity represents the minimum number of steps required to execute an algorithm. It provides us with the **lower bound** of an algorithm.
- **Average-Case Complexity:** The average-case complexity represents the average number of steps required to execute an algorithm. We take the average of the steps executed in all the cases to calculate average-case complexity.

> **Note:** Worst-case complexity is used to find the guarantee in how much time some particular algorithm will finish. This is the most important time complexity. If the type of complexity is not mentioned, then always consider **Worst-Case** time complexity.

---

## Growth of Functions

Let's look at the growth rates of various functions. The size of the input is `n`.

### Constant Time, O(1)

An algorithm is said to run in **constant time** if the output is produced in constant time, regardless of the input size.

**Examples:**

1. Accessing an nth element of a list.
2. Push and pop of a stack.
3. Add and remove from a queue.
4. Accessing an element of a Hash-Table.

### Linear Time, O(n)

An algorithm is said to run in **linear time** if the execution time of the algorithm is directly proportional to the input size.

**Examples:**

1. List operations like search element, find min, find max, etc.
2. Linked list operations like traversal, find min, find max, etc.

> **Note:** If we need to traverse all the nodes of a data structure for some task, then complexity can't be less than O(n).

### Logarithmic Time, O(log(n))

An algorithm is said to run in **logarithmic time** if the execution time of the algorithm is proportional to the logarithm of the input size. In each step of an algorithm, a significant portion (e.g. half portion) of the input is pruned/rejected out without traversing it.

An example is the **Binary Search** algorithm. We will read about this algorithm in this book.

### n·log(n) Time, O(n·log(n))

An algorithm is said to run in **n·log(n) time** if the execution time of an algorithm is proportional to the product of input size and logarithm of the input size. In these algorithms, each time the input is divided into half (or some proportion) and each portion is processed independently.

Examples are **Merge-Sort**, **Quick-Sort** (average case), **Heap-Sort**, etc.

### Quadratic Time, O(n²)

An algorithm is said to run in **quadratic time** if the execution time of an algorithm is proportional to the square of the input size. In these algorithms, each element is compared with all the other elements.

Examples are **Bubble-Sort**, **Selection-Sort**, **Insertion-Sort**.

### Exponential Time, O(2ⁿ)

In these algorithms, all possible subsets of elements of input data are generated. A common example is the **power set**.

### Factorial Time, O(n!)

In these algorithms, all possible permutations of the elements of input data are generated. Finding **permutations** is a common example of factorial time.

### Common Time Complexities

A list of commonly occurring algorithm time complexities in increasing order:

| Name | Notation |
|------|----------|
| Constant | O(1) |
| Logarithmic | O(log(n)) |
| Linear | O(n) |
| N·Log(N) | O(n·log(n)) |
| Quadratic | O(n²) |
| Polynomial | O(nᶜ) — `c` is a constant & `c > 1` |
| Exponential | O(cⁿ) — `c` is a constant & `c > 1` |
| Factorial | O(n!) |
| N-Power-N | O(nⁿ) |

### Growth Rate Comparison

The time taken by certain algorithms to run varies dramatically with the size of the input. Some algorithms take minutes or even seconds to run on huge input, whereas others may take days to complete their execution. To understand how the rate of growth changes with the size of the input in different functions, the following table presents the approximate number of steps required to run an algorithm:

| N | O(1) | O(log(n)) | O(n) | O(n·log(n)) | O(n²) | O(n³) | O(2ⁿ) |
|---|------|-----------|------|-------------|-------|-------|-------|
| 10 | 1 | 3 | 10 | 30 | 10² | 10³ | 10³ |
| 10² | 1 | 6 | 10² | 6×10² | 10⁴ | 10⁶ | 10³⁰ |
| 10³ | 1 | 9 | 10³ | 9×10³ | 10⁶ | 10⁹ | 10³⁰⁰ |
| 10⁴ | 1 | 13 | 10⁴ | 13×10⁴ | 10⁸ | 10¹² | 10³⁰⁰⁰ |
| 10⁵ | 1 | 16 | 10⁵ | 16×10⁵ | 10¹⁰ | 10¹⁵ | 10³⁰⁰⁰⁰ |
| 10⁶ | 1 | 19 | 10⁶ | 19×10⁶ | 10¹² | 10¹⁸ | 10³⁰⁰⁰⁰⁰ |

---

## Deriving an Algorithm's Runtime Function

### Constants

If any line of code is a statement with basic operations — e.g., comparisons, assignments, or reading a variable — they take constant time each. Thus, the time complexity of each statement is **O(1)**.

### Loops

In a loop, a repetition of a particular code happens for `n` times, where `n` is the size of the loop. Every statement inside the loop has a runtime of O(1). The running time of a loop is a product of the running time of the statement inside the loop and the number of iterations in the loop. Time Complexity is **O(n)**.

### Nested Loops

The running time of nested loops is a product of the running time of the statements inside the loop multiplied by a product of the size of all the loops. Time Complexity is **O(nᶜ)**, where `c` is the number of loops. For two loops, it will be **O(n²)**.

### Consecutive Statements

In this case, we add the running time of all the consecutive lines of code.

### If-Else Statement

In this case, either the `if` will run or the `else` will run. So, the block with the larger runtime will be considered.

### Logarithmic Statement

In this case, each iteration will cut the input size into `b` pieces and consider one of the pieces for the next iteration. Time complexity in this situation will be **O(log_b(n))**.

---

## Recursive Function

**Recursion:** A recursive function is a function that calls itself, directly or indirectly.

A recursive method consists of two parts: **Termination Condition** and **Body** (which includes recursive expansion).

1. **Termination Condition:** A recursive method always contains one or more terminating conditions. A condition in which a recursive method processes a simple case and does not call itself.
2. **Body (including recursive expansion):** The main logic of the recursive method is contained in the body of the method. It also contains the recursion expansion statement that, in turn, calls the method itself.
