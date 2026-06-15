# 04 - Sorting

## Bubble Sort

Bubble sort repeatedly steps through the list, compares **adjacent** elements
and swaps them when they are out of order. After each pass the largest remaining
value "bubbles up" to its final position at the end, so each pass can ignore one
more element on the right.

| Case    | Time      | Notes                                   |
| ------- | --------- | --------------------------------------- |
| Best    | O(n)      | Already sorted (early-exit on no swaps) |
| Average | O(n²)     |                                         |
| Worst   | O(n²)     | Reverse sorted                          |
| Space   | O(1)      | In-place, stable                        |

### Files

| File                                       | What it does                                                       |
| ------------------------------------------ | ----------------------------------------------------------------- |
| `01_bubble_sort.py`                        | Plain implementation with the early-exit optimization.            |
| `02_bubble_sort_visualize_terminal.py`     | ASCII bar visualization in the terminal — **no dependencies**.    |
| `03_bubble_sort_visualize_matplotlib.py`   | Animated bar-chart visualization (`pip install matplotlib`).      |

### Run

```bash
python 01_bubble_sort.py
python 02_bubble_sort_visualize_terminal.py      # animated bars in the console
python 03_bubble_sort_visualize_matplotlib.py    # animated window (needs matplotlib)
```

Tune the animation speed with the `DELAY` constant (terminal) or the
`interval=` argument to `FuncAnimation` (matplotlib).
