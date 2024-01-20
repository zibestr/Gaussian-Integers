from numbers import Complex, Integral
import random
from math import cos, sin, log
from abc import ABC, abstractmethod
from typing import TypeAlias


Integer: TypeAlias = int | Integral


class GaussianNumber(Complex, ABC):
    """Abstract Gaussian number"""
    _real: Integer
    _image: Integer

    def __init__(self, real: Integer = 0,
                 imag: Integer = 0) -> None:
        if not ((isinstance(real, int) or isinstance(real, Integral))
                and (isinstance(imag, int) or isinstance(imag, Integral))):
            raise ValueError("a and b must be int")

        self._real = real
        self._imag = imag

    def __complex__(self) -> complex:
        return complex(self._real, self._image)

    @property
    def real(self) -> Integer:
        """Retrieve the real component of this number.
        """
        return self._real

    @real.setter
    def real(self, value: Integer) -> None:
        self._real = value

    @property
    def imag(self) -> Integer:
        """Retrieve the image component of this number.
        """
        return self._imag

    @imag.setter
    def imag(self, value: Integer) -> None:
        self._imag = value

    @abstractmethod
    def __floordiv__(self, other) -> Complex:
        """self // other"""
        raise NotImplementedError

    @abstractmethod
    def __rfloordiv__(self, other) -> Complex:
        """other // self"""
        raise NotImplementedError

    @abstractmethod
    def __mod__(self, other) -> Complex:
        """self % other"""
        raise NotImplementedError

    @abstractmethod
    def __rmod__(self, other) -> Complex:
        """other % self"""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        """self == other"""
        if not isinstance(other, GaussianNumber):
            raise TypeError("cannot compare complex number and %s"
                            % type(other))
        return self.real == other.real and self.imag == other.imag

    def __hash__(self) -> int:
        "Returns hash code for number"
        return hash(self._real) + hash(self._imag)

    def __truediv__(self, other: Complex) -> complex:
        """self / other: Returns complex number (Not a Gaussian)"""
        if (other.real == 0 or other.imag == 0) and \
           (other.real != 0 and other.imag != 0):
            if other.imag == 0:
                new_real = self.real / other.real
                new_imag = self.imag / other.real
            elif other.real == 0:
                new_real = self.imag / other.imag
                new_imag = - self.real / other.imag
        elif other.real == 0 and other.imag == 0:
            raise ZeroDivisionError("complex division by zero complex")
        else:
            numerator_complex: GaussianNumber = self * other.conjugate()
            denominator_num: Integral = other.real ** 2 + other.imag ** 2
            new_real = numerator_complex.real / denominator_num
            new_imag = numerator_complex.imag / denominator_num
        return complex(new_real, new_imag)

    def __rtruediv__(self, other: Complex) -> complex:
        """other / self"""
        return other / self

    def __abs__(self):
        """Returns the norm of complex number."""
        return self.real ** 2 + self.imag ** 2

    def conjugate(self) -> Complex:
        return GaussianInteger(self.real, -self.imag)

    def __pow__(self, exponent: Integer) -> Complex:
        """self**exponent; exponent must be a integer"""
        result: Complex = self
        exponent -= 1
        if exponent == 0:
            return result
        elif exponent < 0:
            raise ValueError("exponent must be not negative")
        else:
            for _ in range(exponent):
                result *= self
        return result

    def __rpow__(self, base: Integer) -> complex:
        """base ** self"""
        # c ^ (a + bj) = c ^ a * (cos(log c) + jsin(log c)) ^ b
        new_complex = complex(cos(log(base)), sin(log(base))) ** self.imag
        return base ** self.real * new_complex

    def __mul__(self, other: Complex) -> Complex:
        """(a1 + b1 * j) * (a2 + b2 * j)"""
        if isinstance(other, Complex):
            other = GaussianInteger(int(other.real),
                                    int(other.imag))
        else:
            raise TypeError("expected complex, got %s" % type(other))
        new_real = self.real * other.real - self.imag * other.imag
        new_imag = self.real * other.imag + other.real * self.imag
        return GaussianInteger(new_real, new_imag)

    def __rmul__(self, other: Complex) -> Complex:
        """other * self"""
        return self * other

    def __add__(self, other: Complex) -> Complex:
        if isinstance(other, Complex):
            other = GaussianInteger(int(other.real),
                                    int(other.imag))
        else:
            raise TypeError("expected complex, got %s" % type(other))
        new_real = self.real + other.real
        new_imag = self.imag + other.imag
        return GaussianInteger(new_real, new_imag)

    def __radd__(self, other: Complex) -> Complex:
        return self.real + other.real

    @property
    @abstractmethod
    def associated(self) -> tuple[Complex, Complex,
                                  Complex]:
        """Returns a tuple of associated gaussian numbers of this."""
        raise NotImplementedError

    @abstractmethod
    def __bool__(self) -> bool:
        """Converts this number to a boolean"""
        raise NotImplementedError

    def __neg__(self) -> Complex:
        return GaussianInteger(-self.real, -self.imag)

    def __pos__(self) -> Complex:
        return GaussianInteger(+self.real, +self.imag)

    def __str__(self) -> str:
        """String representation of this gaussian number"""
        return f"{self.real} " + ("+" if int(self.imag) > 0 else "-") \
            + f" {abs(self.imag)}j"

    def __repr__(self) -> str:
        return self.__str__()


class GaussianInteger(GaussianNumber):
    """
    Provides a gaussian complex integer numbers

    Definition
    ----------
    Gaussian complex integer numbers is numbers of the form:

    z = a + bj, where a and b is a integers
    """
    def __bool__(self) -> bool:
        """Returns True if real and image are not equal zero"""
        return self._real != 0 and self._image != 0

    @property
    def associated(self) -> tuple[Complex, Complex,
                                  Complex]:
        return (self * GaussianInteger(-1, 0),
                self * GaussianInteger(0, 1),
                self * GaussianInteger(0, -1))

    def __floordiv__(self, other: GaussianNumber) -> GaussianNumber:
        """self // other"""
        float_complex: complex = self / other
        new_real = round(float_complex.real)
        new_imag = round(float_complex.imag)
        return GaussianInteger(new_real, new_imag)

    def __rfloordiv__(self, other: GaussianNumber) -> GaussianNumber:
        """other // self"""
        return other // self

    def __mod__(self, other: GaussianNumber) -> GaussianNumber:
        """self % other"""
        return self - other * (self // other)

    def __rmod__(self, other: GaussianNumber) -> GaussianNumber:
        """other % self"""
        return other % self

    @staticmethod
    def random(a: int, b: int,
               seed: int | None = None) -> GaussianNumber:
        """Returns a random gaussian integer number"""
        random.seed(seed)
        real = random.randint(a, b)
        image = random.randint(a, b)
        # Reset random seed
        random.seed(None)
        return GaussianInteger(real, image)
