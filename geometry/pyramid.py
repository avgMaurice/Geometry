def paste(zeilen):
    """
    Prints a pyramid pattern of stars with the given number of rows.

    Args:
        zeilen (int): The number of rows in the pyramid.
    """
    for i in range(zeilen):
        # Leerzeichen ausgeben
        print(" " * (zeilen - i - 1), end="")

        # Sterne ausgeben
        print("*" * (2 * i + 1))


def paste_reverse(zeilen):
    """
    Prints an inverted pyramid pattern of stars with the given number of rows.

    Args:
        zeilen (int): The number of rows in the inverted pyramid.
    """
    for i in range(zeilen - 1, -1, -1):
        # Leerzeichen ausgeben
        print(" " * (zeilen - i - 1), end="")

        # Sterne ausgeben
        print("*" * (2 * i + 1))

