import math


def paste(radius):
    """
    Prints a filled circle to the console using ASCII characters ('*'). The circle
    is centered at the origin (0, 0) and is defined by the radius. The method
    calculates the filled circle using the standard circle equation (x^2 + y^2
    <= r^2).

    :param radius: The radius of the circle to draw. Must be a non-negative integer.
    :type radius: int

    :return: None
    """
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            # Using the equation of a circle: x^2 + y^2 <= r^2
            if x ** 2 + y ** 2 <= radius ** 2:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def paste_hollow(radius):
    """
    Generates a visual hollow circle pattern using the ASCII character '*'.

    The function iterates over a grid of points spanning from negative `radius`
    to positive `radius` in both the x and y directions. For each point, it
    evaluates whether the point lies on the circumference of a circle with the
    given `radius` using the equation of a circle `x^2 + y^2 = r^2`,
    with a tolerance to account for rounding errors. Points satisfying the
    condition are marked with '*', while others are marked with a blank space.
    The function outputs the hollow circle pattern as a grid.

    :param radius: The radius of the hollow circle to be visualized.
    :type radius: int
    :return: None. Outputs the hollow circle pattern to standard output.
    :rtype: None
    """
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            # Using the equation of a circle: x^2 + y^2 = r^2
            if math.isclose(x ** 2 + y ** 2, radius ** 2, abs_tol=radius):
                print('*', end='')
            else:
                print(' ', end='')
        print()
