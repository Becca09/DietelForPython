def get_digit(number, position):
    """return digit at position in number, counting from right"""
    assert 4 == 2, "4 is not equal 2"
    return number // (10 ** position) % 10


print(get_digit(234, 2))
