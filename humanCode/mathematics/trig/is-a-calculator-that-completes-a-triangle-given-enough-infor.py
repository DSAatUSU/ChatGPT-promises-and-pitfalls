"""
Written by Steven Byrnes, http://sjbyrnes.com/

Download: https://pypi.python.org/pypi/trianglesolver/
Source code repository: https://github.com/sbyrnes321/trianglesolver

This little package applies the law of sines or cosines to find all the
sides and angles of a triangle, if you know some of the sides and/or
angles.

The main function defined by this package is solve(...). Simple example::

    from math import pi
    from trianglesolver import solve
    a,b,c,A,B,C = solve(b=7.6, c=8.3, A=pi/3)

Following the usual convention, lower-case letters are side lengths and
capital letters are angles. Corresponding letters are opposite each other,
e.g. side b is opposite angle B.

All angles are in radians! However, you can use the degree constant to
convert::

    from trianglesolver import solve, degree
    a,b,c,A,B,C = solve(b=7, A=5*degree, B=70*degree)
    print(C / degree)
"""

from __future__ import division, print_function
from math import sin, cos, pi, sqrt, acos, asin, isclose

# 5 * degree is 5 degrees in radians
# X / degree is the angle X expressed in degrees
degree = pi / 180

# ---------- Helper functions -------------------------------------- #


def aaas(D, E, F, f):
    """This function solves the triangle and returns (d,e,f,D,E,F)"""
    d = f * sin(D) / sin(F)
    e = f * sin(E) / sin(F)
    return (d, e, f, D, E, F)


def sss(d, e, f):
    """This function solves the triangle and returns (d,e,f,D,E,F)"""
    assert d + e > f and e + f > d and f + d > e
    F = acos((d**2 + e**2 - f**2) / (2 * d * e))
    E = acos((d**2 + f**2 - e**2) / (2 * d * f))
    D = pi - F - E
    return (d, e, f, D, E, F)


def sas(d, e, F):
    """This function solves the triangle and returns (d,e,f,D,E,F)"""
    f = sqrt(d**2 + e**2 - 2 * d * e * cos(F))
    return sss(d, e, f)


def ssa(d, e, D, ssa_flag):
    """This function solves the triangle and returns (d,e,f,D,E,F)
    See docstring for solve() for definition of ssa_flag"""
    assert ssa_flag in ("acute", "obtuse", "forbid"), "Invalid value of ssa_flag"
    sinE = sin(D) * e / d

    # This whole part is to calculate E
    if isclose(sinE, 1):
        # Right triangle, where the solution is unique
        E = pi / 2
    else:
        assert sinE < 1, "No such triangle"
        E_acute = asin(sinE)
        E_obtuse = pi - E_acute
        acute_is_valid = 0 < (pi - D - E_acute) < pi
        obtuse_is_valid = 0 < (pi - D - E_obtuse) < pi

        if ssa_flag == "acute":
            assert acute_is_valid, "No such triangle"
            E = E_acute
        elif ssa_flag == "obtuse":
            assert obtuse_is_valid, "No such triangle"
            E = E_obtuse
        else:
            assert ssa_flag == "forbid"
            if acute_is_valid and obtuse_is_valid:
                raise ValueError("Two different triangles fit this description")
            if (not acute_is_valid) and (not obtuse_is_valid):
                raise ValueError("No such triangle")
            E = E_acute if acute_is_valid else E_obtuse
    # Now that we know E, the rest is straightforward
    F = pi - D - E
    e, f, d, E, F, D = aaas(E, F, D, d)
    return (d, e, f, D, E, F)


# ---------- Main function you should use ------------------------- #


def solve(a=None, b=None, c=None, A=None, B=None, C=None, ssa_flag="forbid"):
    """
    Solve to find all the information about a triangle, given partial
    information.

    a, b, c, A, B, and C are the three sides and angles. (e.g. A is the angle
    opposite the side of length a.) Out of these six possibilities, you need
    to tell the program exactly three. Then the program will tell you all six.

    It returns a tuple (a, b, c, A, B, C).

    "ssa" is the situation when you give two sides and an angle which is not
    between them. This is usually not enough information to specify a unique
    triangle. Usually there are two possible triangles—except for a special
    case with right triangles where the two possible triangles are the same
    (the equation has a "double root"), and some cases where one of the two
    possible triangles has a negative angle.

    Therefore there is an 'ssa_flag'. You can set it to'forbid' (raise an error
    if the answer is not unique - the default setting), or 'acute' (where the
    unknown angle across from the known side is chosen to be acute) or 'obtuse'
    (similarly).
    """
    if sum(x is not None for x in (a, b, c, A, B, C)) != 3:
        raise ValueError("Must provide exactly 3 inputs")
    if sum(x is None for x in (a, b, c)) == 3:
        raise ValueError("Must provide at least 1 side length")
    assert all(x > 0 for x in (a, b, c, A, B, C) if x is not None)
    assert all(x < pi for x in (A, B, C) if x is not None)
    assert ssa_flag in ("forbid", "acute", "obtuse")

    # If three sides are known...
    if sum(x is not None for x in (a, b, c)) == 3:
        a, b, c, A, B, C = sss(a, b, c)
        return (a, b, c, A, B, C)

    # If two sides and one angle are known...
    if sum(x is not None for x in (a, b, c)) == 2:
        # ssa case
        if all(x is not None for x in (a, A, b)):
            a, b, c, A, B, C = ssa(a, b, A, ssa_flag)
        elif all(x is not None for x in (a, A, c)):
            a, c, b, A, C, B = ssa(a, c, A, ssa_flag)
        elif all(x is not None for x in (b, B, a)):
            b, a, c, B, A, C = ssa(b, a, B, ssa_flag)
        elif all(x is not None for x in (b, B, c)):
            b, c, a, B, C, A = ssa(b, c, B, ssa_flag)
        elif all(x is not None for x in (c, C, a)):
            c, a, b, C, A, B = ssa(c, a, C, ssa_flag)
        elif all(x is not None for x in (c, C, b)):
            c, b, a, C, B, A = ssa(c, b, C, ssa_flag)

        # sas case
        elif all(x is not None for x in (a, b, C)):
            a, b, c, A, B, C = sas(a, b, C)
        elif all(x is not None for x in (b, c, A)):
            b, c, a, B, C, A = sas(b, c, A)
        elif all(x is not None for x in (c, a, B)):
            c, a, b, C, A, B = sas(c, a, B)
        else:
            raise ValueError("Oops, this code should never run")
        return (a, b, c, A, B, C)

    # If one side and two angles are known...
    if sum(x is not None for x in (a, b, c)) == 1:
        # Find the third angle...
        if A is None:
            A = pi - B - C
        elif B is None:
            B = pi - A - C
        else:
            C = pi - A - B
        assert A > 0 and B > 0 and C > 0
        # Then solve the triangle...
        if c is not None:
            a, b, c, A, B, C = aaas(A, B, C, c)
        elif a is not None:
            b, c, a, B, C, A = aaas(B, C, A, a)
        else:
            c, a, b, C, A, B = aaas(C, A, B, b)
        return (a, b, c, A, B, C)
    raise ValueError("Oops, this code should never run")


# ---------------- Tests ------------------------------------------------- #


def tuple_isclose(x, y):
    return all(isclose(x[i], y[i]) for i in range(len(x)))


def test_triangle(a, b, c, A, B, C):
    """Check that the triangle satisfies the law of cosines and law of
    sines"""
    assert isclose(a / sin(A), b / sin(B))
    assert isclose(a / sin(A), c / sin(C))
    assert isclose(c**2, a**2 + b**2 - 2 * a * b * cos(C))
    assert isclose(a**2, b**2 + c**2 - 2 * b * c * cos(A))
    assert isclose(b**2, c**2 + a**2 - 2 * c * a * cos(B))


if __name__ == "__main__":
    a = input("Input side a (enter for none): ")
    if a == "":
        a = None
    else:
        a = int(a)

    b = input("Input side b (enter for none): ")
    if b == "":
        b = None
    else:
        b = int(b)

    c = input("Input side c (enter for none): ")
    if c == "":
        c = None
    else:
        c = int(c)

    A = input("Input angle A in radians (enter for none): ")
    if A == "":
        A = None
    else:
        A = int(A)

    B = input("Input angle B in radians (enter for none): ")
    if B == "":
        B = None
    else:
        B = int(B)

    C = input("Input angle C in radians (enter for none): ")
    if C == "":
        C = None
    else:
        C = int(C)

    a, b, c, A, B, C = solve(a=a, b=b, c=c, A=A, B=B, C=C)

    print("Side a: " + str(a))
    print("Side b: " + str(b))
    print("Side c: " + str(c))
    print("Angle A: " + str(A))
    print("Angle B: " + str(B))
    print("Angle C: " + str(C))
