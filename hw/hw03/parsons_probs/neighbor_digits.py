def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10 : return int(num == prev_digit)
    left = num // 10
    right = num % 10
    return neighbor_digits(left, right) + int(left % 10 == right or right == prev_digit)