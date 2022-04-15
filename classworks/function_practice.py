def get_digit(number: int, position: int) -> int:
    """
    return digit at position in number, counting from right
    >>> get_digit(234, 0)
    4
    >>> get_digit(234, 2)
    2
    >>> "hello"
    'hello'
    >>> '2' + 3 # doctest: +IGNORE_EXCEPTION_DETAIL
    5
    Traceback (most recent call last):
        ...
    TypeError: can only concatenate str (not "int") to str
    """
    return number // (10 ** position) % 10


get = get_digit(234, 2)
print(get)
