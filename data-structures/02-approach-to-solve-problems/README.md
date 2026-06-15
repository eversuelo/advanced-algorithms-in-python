# Chapter 2: Approach to Solve Problems

## Table of Contents

- [Introduction](#introduction)
- [Constraints](#constraints)
- [Idea Generation](#idea-generation)
  - [Try to simplify the task at hand](#try-to-simplify-the-task-at-hand)
  - [Try a few examples](#try-a-few-examples)
  - [Think of a suitable data-structure](#think-of-a-suitable-data-structure)
  - [Think about similar problems you have already solved](#think-about-similar-problems-you-have-already-solved)
- [Complexities](#complexities)
- [Coding](#coding)
- [Testing](#testing)
- [Example](#example)
- [Summary](#summary)

---

## Introduction

Theoretical knowledge of the algorithm is essential, but it is insufficient. When an interviewer asks the interviewee to solve a problem, then the interviewee can use our five-step approach to solve problems. If you master this technique, you will outperform the majority of applicants in interviews.

Five steps for solving algorithm design questions are:

1. **Constraints**
2. **Ideas Generation**
3. **Complexities analysis**
4. **Coding**
5. **Testing**

---

## Constraints

Solving a technical question is not just about knowing the algorithms and designing a good software system. The interviewer is interested in seeing your approach to any given problem. Often, people make mistakes by failing to ask clarifying follow-up questions about a given problem. They make a lot of assumptions at once and start working with them. Before you start solving a problem, you need to collect a lot of missing information from your interviewer.

In this step, you will write down all the problem's constraints. Never attempt to solve a problem that isn't completely defined. Interview questions are not like exam paper questions, where all the details about a problem are well-defined. The interviewer wants you to ask questions and clarify the problem during the interview.

Suppose, when the interviewer says to write an algorithm to sort numbers. You need to ask the following clarifying questions:

1. The first thing you need to know is what sort of data is being given. Assume the interviewer gives you the answer: **Integer**.
2. The size of the data is the second piece of information you need to know. If the input data is 100 integers or 1 billion integers, the algorithm is different.

### Constraints for a list of numbers

1. How many elements are there in the list?
2. What is the range of value in each element? What is the min and max value?
3. What is the kind of data in each element? Is it an integer or a floating point?
4. Does the list contain unique data or not?

### Constraints for a list of strings

1. How many total elements are there in the list?
2. What is the length of each string? What is the min and max length?
3. Does the list contain unique data or not?

### Constraints for a Graph

1. How many nodes are there in the graph?
2. How many edges are there in the graph?
3. Is it a weighted graph? What is the range of weights?
4. Does the graph have directed edges, or undirected edges?
5. Does the graph have a loop?
6. Does the graph have a negative sum loop?
7. Are there any self-loops in the graph?

We will see in the graph chapter that depending upon the constraints, the algorithm applied changes and so does the complexity of the solution.

---

## Idea Generation

We will cover a lot of theoretical knowledge in this book. It is impossible to cover all the questions, as new questions are created every day. Therefore, you should know how to handle new problems. Even if you know the solution to the problem asked by the interviewer, you still need to have a discussion with the interviewer and try to reach the solution. You need to analyse the problem also because the interviewer may modify a question a bit, so the approach to solve it will vary.

**How to solve an unseen problem?** The solution to this problem is to learn a lot, and the more you practice, the more you will be able to answer any unseen problem. When you've solved enough problems, you'll see a pattern in the questions and be able to answer unseen problems with ease.

Following is the strategy that you need to follow to solve an unknown problem:

1. Try to simplify the task at hand.
2. Try a few examples.
3. Think of a suitable data structure.
4. Think about similar problems that you have already solved.

### Try to simplify the task at hand

Let's look into the following problem: Husbands and wives are standing at random in a line. Husbands have been numbered H1, H2, H3 and so on. Wives have been numbered W1, W2, W3 and so on. You need to arrange them so that H1 will stand first, followed by W1, then H2 followed by W2 and so on.

At first look, it looks complicated, but it is a simple problem. Try to find a relation to the final position:

```
P(Hi) = i * 2 - 1
P(Wi) = i * 2
```

We are leaving an exercise for you to do something like Insertion-Sort for the rest of the algorithm, and you are done.

### Try a few examples

In the above problem, if you try it with an example of three husband-wife pairs, then you can get the same formula as shown in the previous section. Using more examples will also assist in solving the problem.

### Think of a suitable data-structure

It's simple to figure out which data structure would be more appropriate for some specific problems. Throughout this book, we will see a variety of data structures. We must determine which data structure would best meet our requirements.

**Problem 1:** If we want to find the minimum and maximum of a given sequence.

> **Analysis:** The heap is most likely the data structure we're searching for.

**Problem 2:** We are given a stream of data; at any time, we can be asked to tell the median value of the data, and maybe we can be asked to pop median data.

> **Analysis:** We may visualise a tree, maybe a balanced tree with the median at the root. Wait a minute! It's not straightforward to ensure that the tree root is a median.
>
> We can't get the median from a heap, although it can give us the minimum or maximum. What if we use two heaps, a max-heap and a min-heap? The max-heap will hold the smaller values, while the min-heap will have the larger values. Furthermore, we will keep track of how many elements are in the heaps. It would help if you came up with the rest of the algorithm on your own.

For every unseen problem, think about the data structures you know, and maybe one of them or some combination of them will solve your problem.

### Think about similar problems you have already solved

**Problem 3:** Given head pointers of two linked lists that intersect at some point. Find the point of intersection. However, in place of the end of the linked list being a null pointer, there is a loop.

> **Analysis:** You know how to find the intersection point of two intersecting linked lists, and you know how to find if a linked list has a loop (three-pointer solution). Therefore, you can combine both solutions to solve the problem at hand.

---

## Complexities

Solving a problem is not just finding a correct solution. The solution should be fast and should have reasonable memory requirements. In the previous chapters, you learned about big-O notation. You should be able to perform Big-O analysis. If you believe the solution you have provided is not optimal and there is a better solution, then try to figure it out.

Most interviewers expect that you should be able to find the Time and Space Complexity of the algorithms. You should be able to calculate the Time and Space Complexity quickly. Whenever you are solving any problem, you should find the complexity associated with it. From this, you would be able to choose the best solutions. In some problems there are some trade-offs between Space and Time Complexity, so you should know these trade-offs. Taking a little extra space will save you a lot of time and make your algorithm much faster.

---

## Coding

At this stage, you have already captured all the constraints of the problem, suggested a few solutions, evaluated the complexities of those solutions and selected the one for final coding. Never begin coding without first discussing with the interviewer about constraints, idea generation and complexity.

We are used to writing code in an IDE like Visual Studio. So several people struggle when asked to write code on a whiteboard or some blank sheet. Therefore, you should do some practice coding on a sheet of paper. You should think before coding because there is no back button on the sheet of paper.

Always try to write modular code. Small functions need to be created so that the code is clean and managed. If there is a requirement for a swap function, just use this function and tell the interviewer that you will write it later. Everybody knows that you can write a swap function.

---

## Testing

You're not done even if the code is written. It is essential to validate the code using a variety of small test cases. It shows that you understand the importance of testing. It also gives the interviewer confidence that you would not write a bug-ridden program. Once you have finished coding, you should go over the code line-by-line for some small test cases. This is to ensure that the code is functioning as intended.

Following are some test cases to check:

- **Normal test cases:** These are the positive test cases, which contain the most common scenario, and the emphasis is on the functioning of the code's base logic.

  For example, if we are solving some problems for a linked list, then this test may contain what happens when a linked list with three or four nodes is given as input. Before declaring the code complete, you should always think about these test cases.

- **Edge cases:** These are the test cases which are used to test the boundaries of the code. Edge cases can help to make your code more robust. We must add checks in the code to handle edge cases.

  For example, we can generate edge cases with the same linked list algorithm to see how the code reacts when an empty list or only one node is passed.

> **Note:** Always follow these five steps, never jump to coding before doing constraint analysis, idea generation, and complexity analysis. At last, never miss the testing step.

---

## Example

Let us suppose the interviewer asks you to give the best sorting algorithm.

Some interviewees will directly jump to Quick-Sort `O(n.log(n))`. Oops, mistake! You need to ask many questions before beginning to solve this problem.

Let's look at these questions one by one:

| # | Question | Answer |
|---|----------|--------|
| 1 | What is the kind of data? Are they integers? | Yes, they are integers. |
| 2 | How much data are we going to sort? | Maybe thousands. |
| 3 | What exactly is this data about? | They store a person's age. |
| 4 | What kind of data structure is used to hold this data? | Data are given in the form of a list. |
| 5 | Can we modify the given data structure? (and many more…) | No, you cannot modify the data structure provided. |

So, we are all set to use the given information to make a perfect solution:

- From the **first** answer, we know the type of data is integer.
- From the **second** answer, the data size is limited — only some thousands.
- From the **third** answer, it's age-related data, so we can assume a person's age will be between 1 to 150.
- From the **fourth/fifth** answers, data is in the form of a list and cannot be changed.

To summarise, we can use **bucket sort** to sort the data. Since the range is only 1–150, we only need an integer list of 150 elements. We don't have to think about data overflow because the data is in the thousands, and we get the solution in **linear time**.

---

## Summary

At this point, you know the process of handling unseen problems very well. In the coming chapters, we will be looking into various data structures and the problems they solve. It may be possible that you cannot understand some portion of this chapter, as knowledge of the rest of the book is needed, so you can reread this chapter after reading the rest of the data structures portion.

A huge number of problems are solved in this book. However, it is recommended that you first try to solve them yourself and then look for the solution. Always think about the complexity of the problem. In the interview, interaction is the key to get the problem described completely and discuss your approach with the interviewer.
