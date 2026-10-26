def insertion_sort_decreasing(arr):
    """Sort a list in monotonically decreasing order (in place)."""
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # Shift elements smaller than key one position to the right
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr