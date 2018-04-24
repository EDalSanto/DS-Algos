def swap(arr, first_index, second_index):
    temp = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temp

# inefficient would be arr.index(min(arr))
def index_of_minimum(arr, starting_index):
    min_index = starting_index
    min_value = arr[starting_index]

    for index in range(starting_index, len(arr)):
        current_value = arr[index]

        if current_value < min_value:
            min_index = index
            min_value = current_value

    return min_index

print(index_of_minimum([1,2,3,0], 0) == 3)
print(index_of_minimum([1,2,3,0], 2) == 3)


def selection_sort(arr):
    array_up_last_two_elements = arr[0:-2]

    for index in range(len(array_up_last_two_elements)):
        index_of_minimum_in_subarray = index_of_minimum(arr, index + 1)
        swap(arr, index, index_of_minimum_in_subarray)



arr = [22, 11, 99, 88, 9, 7, 42]
selection_sort(arr)
print(arr == [7, 9, 11, 22, 42, 88, 99])
