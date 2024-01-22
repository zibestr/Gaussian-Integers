from ._base import GaussianInteger
from math import ceil, floor, sqrt
from numbers import Complex
from typing import Callable


def round_complex(z: complex) -> GaussianInteger:
    """Round complex number to the nearest gaussian integer"""
    complex_grid = (
        GaussianInteger(floor(z.real), floor(z.imag)),
        GaussianInteger(floor(z.real), ceil(z.imag)),
        GaussianInteger(ceil(z.real), floor(z.imag)),
        GaussianInteger(ceil(z.real), ceil(z.imag))
    )
    compare_dict = {complex_distance(z, complex_grid[i]): complex_grid[i]
                    for i in range(len(complex_grid))}
    min_key = min(compare_dict.keys())

    return compare_dict[min_key]


def complex_distance(z1: complex | Complex, z2: complex | Complex) -> float:
    """
    Calculate Euclidean distance between two complex\\
    numbers on complex plane
    """
    return sqrt((z1.real - z2.real) ** 2 + (z1.imag - z2.imag) ** 2)


def __is_real_prime__(x: int) -> bool:
    """Check if real integer number is prime"""
    for d in range(2, ceil(sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True


def __gauss_criterion1__(z: GaussianInteger) -> bool:
    """
    Check if Gaussian number is prime by criterion:

        - one of real, image parts is zero and the absolute value of the other
        is a prime number of the form 4n + 3
    """
    a = z.real
    b = z.imag
    criterion: Callable = lambda x1, x2: x1 == 0 and \
        __is_real_prime__(abs(x2)) and (abs(x2) - 3) % 4 == 0
    return criterion(a, b) or criterion(b, a)


def __gauss_criterion2__(z: GaussianInteger) -> bool:
    """
    Check if Gaussian number is prime by criterion:

        - real and image parts are nonzero and norm is a prime number (which
        will not be of the form 4n + 3)
    """
    return z.real != 0 and z.imag != 0 and __is_real_prime__(abs(z))


def is_prime(z: GaussianInteger) -> bool:
    if not isinstance(z, GaussianInteger):
        raise TypeError("number must be a gaussian integer")
    return __gauss_criterion1__(z) or __gauss_criterion2__(z)
