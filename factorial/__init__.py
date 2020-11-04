"""Demo module"""
def factorial(num: int) -> int:
    """Factorial Function
    https://en.wikipedia.org/wiki/factorial
    """
    # Written by @studentofkyoto
    if not isinstance(num, int):
        raise TypeError
    if num == 0:
        return 1
    return num * factorial(num - 1)
