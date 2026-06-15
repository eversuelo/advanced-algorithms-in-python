# Bubble Sort -> Animated bar-chart visualization with matplotlib
#
# Requires: pip install matplotlib
#
# Uses a generator that "yields" the array state after every comparison
# and swap. matplotlib's FuncAnimation then renders each yielded state
# as a frame, highlighting the two bars being compared in red.

import random

try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
except ImportError:
    raise SystemExit("This demo needs matplotlib. Install it with: pip install matplotlib")


def bubble_sort_steps(arr):
    """Yield (array, i, j) snapshots so each step can be drawn as a frame."""
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            yield arr.copy(), j, j + 1          # before compare/swap
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr.copy(), j, j + 1      # after swap
        if not swapped:
            break
    yield arr.copy(), -1, -1                     # final sorted state


def visualize(data):
    fig, ax = plt.subplots()
    ax.set_title("Bubble Sort Visualization")
    bars = ax.bar(range(len(data)), data, color="steelblue")
    ax.set_ylim(0, max(data) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    frames = list(bubble_sort_steps(data.copy()))

    def update(frame):
        arr, a, b = frame
        for idx, bar in enumerate(bars):
            bar.set_height(arr[idx])
            if idx in (a, b):
                bar.set_color("crimson")        # bars being compared
            else:
                bar.set_color("steelblue")
        text.set_text(f"comparisons frame {frames.index(frame) + 1}/{len(frames)}")
        return bars

    anim = animation.FuncAnimation(
        fig, update, frames=frames, interval=120, repeat=False, blit=False
    )
    plt.show()
    # To save instead of showing, comment out plt.show() and use:
    # anim.save("bubble_sort.gif", writer="pillow", fps=8)


if __name__ == "__main__":
    data = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    # For a longer demo, try a random list:
    # data = random.sample(range(1, 50), 25)
    visualize(data)
