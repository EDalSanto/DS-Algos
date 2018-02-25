# recursive backtrack => at 1 level make all the possible choices
# infinitely adds for loops to the stack

# N = length of string
# time complexity => O(N!), space_complexity => O(N)
# max stack size from recursion => N
def permutations_of_string(chars, result_string):
    """
    Parameters
    chars: characters of string
    result_string: potential permuted string

    Algorithm
    Base case: all chars are in result string
    Iterate through all characters in string
    Add char to result string
    Recursively call of new state

    Big O
    N = length of string
    time complexity ~ O(N!)
    space complexity ~ O(N) (constrained by N)
    """
    if all(slot == None for slot in chars):
        print(''.join(result_string)) # we must have a full result string
    for char_i, char in enumerate(chars):
        # Swap current char to string result
        result_string.append(char)
        chars.pop(char_i)

        # Add new state to the stack
        permutations_of_string(chars, result_string)

        # Backtrack
        result_string.pop()
        chars.insert(char_i, char)

# permutations_of_string(['A', 'B', 'C'], [])
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA


def combinations_fixed_length_string(chars, result_string, length):
    """
    Parameters
    chars: characters of string to make combinations of
    result_string: string of length length to print
    length: how long each combination should be

    Algorithm
    Base case: result string of length length
    Iterate through all chars

    """
    if len(result_string) == length:
        print(''.join(result_string))
        return # we've found a solution / leaf node
    for char in chars:
        # expand path
        result_string.append(char)

        # recursive call
        combinations_fixed_length_string(chars, result_string, length)

        # backtrack
        result_string.pop()


# combinations_fixed_length_string(['A', 'B', 'C'], [], 2)
# AB
# AC
# AA
# BA
# BC
# BB
# CA
# CB
# CC
