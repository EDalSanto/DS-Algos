def merge(arr, l, r, m):
    # copy low and high half over
    low_half = arr[l:(m + 1)]
    high_half = arr[(m + 1):(r + 1)]

    # pointers in new copies
    low_pointer = 0
    high_pointer = 0

    # pointer in arr to write to
    res_pointer = l

    while low_pointer < len(low_half) and high_pointer < len(high_half):
        # copy over min of two
        if low_half[low_pointer] < high_half[high_pointer]:
            arr[res_pointer] = low_half[low_pointer]
            low_pointer += 1
        else: # min is in high half
            arr[res_pointer] = high_half[high_pointer]
            high_pointer += 1

        res_pointer += 1

    # copy over rest
    while low_pointer < len(low_half):
        arr[res_pointer] = low_half[low_pointer]
        low_pointer += 1
        res_pointer += 1

    while high_pointer < len(high_half):
        arr[res_pointer] = high_half[high_pointer]
        high_pointer += 1
        res_pointer += 1



def merge_sort(arr, l, r):
    if r > l:
        # midway point
        m = (l + r) // 2
        # sort left half
        merge_sort(arr, l, m)
        # sort right half
        merge_sort(arr, m + 1, r)
        # combine
        merge(arr, l, r, m)


array = [9, 8, 42, 15, 0, 3, 2, 1]
merge_sort(array, 0, len(array) - 1)
print(array == [0, 1, 2, 3, 8, 9, 15, 42])
