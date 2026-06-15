# Bubble Sort -> Terminal (ASCII) visualization
#
# Draws the array as vertical bars after every comparison so you can
# watch the largest values "bubble" to the right in real time.
# Pure standard library: no extra packages required.

import os
import time

DELAY = 0.08  # seconds between frames; lower = faster


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def draw(arr, j, sorted_from, done=False):
    clear()
    height = max(arr)
    # Draw rows from the top (tallest) down to the baseline
    for level in range(height, 0, -1):
        row = ""
        for idx, value in enumerate(arr):
            if value >= level:
                # Highlight the two bars currently being compared
                if not done and idx in (j, j + 1):
                    row += " * "
                else:
                    row += " | "
            else:
                row += "   "
        print(row)
    # Value labels under each bar
    print("".join(f"{v:^3}" for v in arr))

    if done:
        print("\nSorted!")
    else:
        compared = f"comparing index {j} and {j + 1}"
        locked = f"{sorted_from} element(s) in final position" if sorted_from else ""
        print(f"\n{compared}   {locked}")
    time.sleep(DELAY)


def bubble_sort_visual(arr):
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            draw(arr, j, i)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw(arr, j, i)
        if not swapped:
            break
    draw(arr, 0, size, done=True)
    return arr


if __name__ == "__main__":
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    bubble_sort_visual(array)
    print("Result:", array)
