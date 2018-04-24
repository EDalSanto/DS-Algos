# all elements from right_index to the left are sorted
# value is the value at right_index + 1 currently
def insert(array, right_index, value):
    # starting at value of array at right index..
    i = right_index

    while array[i] > value and i >= 0:
        # slide array[right_index] over 1 position
        array[i + 1] = array[i]
        i -= 1
    array[i + 1] = value



def insertion_sort(array):
    # first element will always be equivalent to a sorted array
    for i in range(0, len(array) - 1):
        insert(array, i, array[i + 1])


array = [ 9, 12, 3, 5, 8, 2, 2, 4, 1 ]
insertion_sort(array)
print(array == [ 1, 2, 2, 3, 4, 5, 8, 9, 12 ])

array2 = [22, 11, 99, 88, 9, 7, 42]
insertion_sort(array2)
print(array2)


array3 = [22, 11, 0, 99, 88, 9, 7, 42]
insertion_sort(array3)
print(array3)
