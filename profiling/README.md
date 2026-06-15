# Profiling in Python

Recognizing the slow parts of your program is the single most important task when it
comes to speeding up your code. In most cases, the code that causes the application to
slow down is a very small fraction of the program. By identifying these critical
sections, you can focus on the parts that need the most improvement without wasting time
in micro-optimization.

**Profiling** is a technique that allows us to pinpoint the most resource-intensive parts
of an application. A **profiler** is a program that runs an application and monitors how
long each function takes to execute, thus detecting the functions on which your
application spends most of its time.

## The optimization workflow

Optimization should always come last. Follow these three steps in order:

1. **Make it run** — We have to get the software in a working state and ensure that it
   produces the correct results. This exploratory phase serves to better understand the
   application and to spot major design issues in the early stages.

2. **Make it right** — We want to ensure that the design of the program is solid.
   Refactoring should be done before attempting any performance optimization. This really
   helps separate the application into independent and cohesive units that are easy to
   maintain.

3. **Make it fast** — Once our program is working and well structured, we can focus on
   performance optimization. We may also want to optimize memory usage if that
   constitutes an issue.

> **Premature optimization is the root of all evil.** Never optimize code you haven't
> measured. Intuition about *where* a program is slow is almost always wrong — measure
> first, then optimize the part that actually matters.

## The example: a particle simulator

To demonstrate profiling, we use a **particle simulator**. The application takes a number
of particles and simulates their movement over time according to a set of laws: each
particle rotates around a central point at a speed proportional to its distance from that
center (like points on a spinning disk). After running the simulation we can verify the
result and, crucially, *measure* how long it takes.

See [`particle_simulator.py`](./particle_simulator.py) for the implementation.

```bash
# Run the simulation (also runs a small correctness test first)
python particle_simulator.py
```

## Profiling tools

### 1. `time` — coarse, whole-program timing

The simplest baseline. On Unix you can use the shell `time` command:

```bash
$ time python particle_simulator.py
real    0m3.159s   # wall-clock time you actually waited
user    0m3.140s   # CPU time spent in your code
sys     0m0.010s   # CPU time spent in the kernel (I/O, syscalls)
```

`real` is the elapsed wall-clock time; `user` + `sys` is total CPU time. If `real` is
much larger than `user`, your program is waiting (I/O, contention) rather than computing.

**On Windows** there is no `time` command. Use PowerShell's `Measure-Command`:

```powershell
Measure-Command { python particle_simulator.py }
```

Cross-platform, you can also wrap the call with `time.perf_counter()` from inside Python:

```python
import time
start = time.perf_counter()
simulator.evolve(0.1)
print(f"elapsed: {time.perf_counter() - start:.3f}s")
```

### 2. `timeit` — reliable micro-benchmarks

`timeit` runs a snippet many times and reports the best result, smoothing out noise. Great
for comparing two implementations of the same small piece of code.

```bash
python -m timeit -s "from particle_simulator import benchmark" "benchmark()"
```

```python
import timeit
timeit.timeit("benchmark()", setup="from particle_simulator import benchmark", number=10)
```

### 3. `cProfile` — function-level profiling

The standard library profiler. It tells you how many times each function was called and
how much time was spent in each (`tottime` = time in the function itself, `cumtime` =
time including sub-calls).

```bash
# Sort by cumulative time
python -m cProfile -s cumulative particle_simulator.py

# Save stats to a file for later inspection
python -m cProfile -o prof.out particle_simulator.py
```

Inspect a saved run interactively:

```python
import pstats
p = pstats.Stats("prof.out")
p.sort_stats("cumulative").print_stats(10)   # top 10 by cumulative time
```

Visualize the call graph with **SnakeViz**:

```bash
pip install snakeviz
snakeviz prof.out
```

### 4. `line_profiler` — line-by-line profiling

Once `cProfile` points you at the hot function, `line_profiler` shows the time spent on
*each line* inside it. Decorate the function with `@profile` and run with `kernprof`:

```bash
pip install line_profiler
kernprof -l -v particle_simulator.py
```

### 5. `memory_profiler` — memory usage

To profile memory rather than time, decorate a function with `@profile` and run:

```bash
pip install memory_profiler
python -m memory_profiler particle_simulator.py
```

## Reading the results

When you profile the particle simulator, you will typically find that almost all the time
is spent inside the inner loop of `ParticleSimulator.evolve` — the part that updates every
particle's position on every timestep. That single, small section is the **bottleneck**:
the place where optimization effort pays off. Everything else (setup, validation,
plotting) is noise by comparison.

This is the whole point of profiling: it turns "the program feels slow" into "line 42 of
`evolve` accounts for 95% of the runtime," so you know exactly where to act.
