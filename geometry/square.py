def paste(size):
    """
    Prints a square pattern of asterisks with the specified size.

    This function generates a square pattern where each side consists
    of a total of `size` asterisks and displays it on the standard output.

    :param size: The size of the square's side. Must be a positive integer.

    :return: None. The function does not return a value as it operates by printing directly.
    """
    for i in range(size):
        print("*" * size)

def paste_hollow(size):
    """
    Prints a hollow square of asterisks of a given size.

    This function generates a square pattern using asterisks (*). The first and
    last rows of the square are filled with asterisks, while the rows in between
    have asterisks only at the borders, leaving the inside hollow. The size
    of the square is specified by the input parameter.

    :param size: The size of the square to be generated. Must be a positive
        integer. Determines both the width and height of the square.
    :type size: int
    :return: None. The function directly prints the hollow square pattern
        to the console.
    :rtype: None
    """
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")