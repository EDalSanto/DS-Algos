def fib_recursive(n):
    """
    More elegant but require O(2^n) time complexity and O(N) space
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """
    less elegant but provides O(N) time and O(1) space
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(fib_iterative(2))
