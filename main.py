def factorial(n: int) -> int:
    """This function calculates the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the number.

    Raises:
        TypeError: If n is not an integer.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
        >>> factorial(1.5)
        Traceback (most recent call last):
            ...
        TypeError: n must be an integer
    """
    # Raise Error if n is not an integer
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
