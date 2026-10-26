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



if __name__ == "__main__":
    tests = [
        [5, 2, 4, 6, 1, 3],
        [31, 41, 59, 26, 41, 58],
        [1],
        [],
        [3, 3, 3],
        [1, 2, 3, 4, 5],
    ]
    for t in tests:
        original = t.copy()
        result = insertion_sort_decreasing(t)
        assert result == sorted(original, reverse=True)
        print(f"{original} -> {result}")
    print("All tests passed!")