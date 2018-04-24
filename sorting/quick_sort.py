def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def partition(arr, l, r):
    # initialize pivot as rightmost element in arr, arr[r]
    pivot_value = arr[r]
    # starting index for elements to left of pivot
    left = l
    # starting index for elements to right of pivot
    right = l
    # starting index for unknown elements
    unknown = l

    for i in range(l, r):
        if arr[i] > pivot_value:
            # move unknown over
            unknown += 1
        else: # current element is less than pivot
            # swap left most gt pivot value
            swap(arr, right, i)
            # increment rightmost
            right += 1
            # unknown again shrinks
            unknown += 1

    # place pivot to leftmost place of gt
    swap(arr, right, r)

    # return pivot location
    return right


def quick_sort(arr, l, r):
    if l < r:
        partition_index = partition(arr, l, r)
        # partitioned element already in correct spot so ignore
        quick_sort(arr, l, partition_index - 1)
        quick_sort(arr, partition_index + 1, r)



array = [ 11, 9, 7, 1, 5, 42, 0, -43 ]
quick_sort(array, 0, len(array) - 1)
print(array)
