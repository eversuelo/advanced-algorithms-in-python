# Bubble Sort -> Time Complexity O(n^2), Space Complexity O(1)
#
# Bubble sort repeatedly steps through the list, compares adjacent
# elements and swaps them if they are in the wrong order. After each
# full pass the largest remaining element "bubbles up" to its final
# position, so the inner loop can shrink by one every pass.


def greater(a, b):
    return a > b


def bubble_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        swapped = False
        for j in range(size - i - 1):
            if greater(arr[j], arr[j + 1]):
                # Swapping
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Optimization: if no swaps happened, the array is already sorted
        if not swapped:
            break
    return arr


# Testing Code
if __name__ == "__main__":
    array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    print("Before:", array)
    bubble_sort(array)
    print("After: ", array)
