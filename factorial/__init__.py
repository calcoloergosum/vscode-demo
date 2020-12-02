"""Module for demo"""
def factorial(num: int) -> int:
    """calculates factorial
    https://en.wikipedia.org/wiki/Factorial
    """
    if not isinstance(num, int):
        raise TypeError()
    if num > 100:
        raise ValueError(f"given {num} is too big")
    if num == 0:
        return 1
    if num < 0:
        raise ValueError("Negative value not allowed")
    return num * factorial(num - 1)
