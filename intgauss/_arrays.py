from ._base import GaussianInteger
from . import gauss_zero
from collections.abc import Sequence, Collection, Callable
from typing import Iterator
from operator import (
    __add__, __sub__,
    __mul__, __truediv__,
    __floordiv__, __mod__
)


class GaussianArray(Collection):
    """Represents a vectorized 1D array of gaussian numbers"""
    __container__: list
    __size__: int

    def __init__(self, *values: *Sequence[GaussianInteger]):
        """Construct a GaussianArray from a sequence of Gaussian numbers"""
        for value in values:
            if not isinstance(value, GaussianInteger):
                raise TypeError("Expected gaussian integer, got %s"
                                % type(value).__name__)
        self.__container__ = list(values)
        self.__size__ = len(values)

    def __getitem__(self, ind: int) -> GaussianInteger:
        try:
            return self.__container__[ind]
        except IndexError:
            raise IndexError("Index out of range: %s" % ind)

    def __setitem__(self, ind: int, value: GaussianInteger) -> None:
        if not isinstance(value, GaussianInteger):
            raise ValueError("excepted a gaussian integer, but got: %s"
                             % type(value).__name__)
        try:
            self.__container__[ind] = value
        except IndexError:
            raise IndexError("Index out of range: %s" % ind)

    def __len__(self) -> int:
        return self.__size__

    def __contains__(self, item) -> bool:
        if not isinstance(item, GaussianInteger):
            raise TypeError("item must be gaussian integer")
        return item in self.__container__

    def __iter__(self) -> Iterator[GaussianInteger]:
        return iter(self.__container__)

    def __reversed__(self) -> Iterator[GaussianInteger]:
        return reversed(self.__container__)

    def __bin_operation__(self, other: Collection,
                          operation: Callable) -> Collection:
        if not isinstance(other, GaussianArray):
            raise TypeError("missing implementation operation for gaussian"
                            "array and %s" % type(other).__name__)
        if len(self) != len(other):
            raise ValueError("arrays must be same length")
        result = list()
        for z1, z2 in zip(self.to_list(), other.to_list()):
            result.append(operation(z1, z2))
        return GaussianArray(*result)

    def __add__(self, other: Collection) -> Collection:
        """Addition of two arrays"""
        return self.__bin_operation__(other, __add__)

    def __neg__(self) -> Collection:
        """Returns negative array"""
        result = list()
        for z1 in self.to_list():
            result.append(-z1)
        return GaussianArray(*result)

    def __sub__(self, other: Collection) -> Collection:
        """Subtract of two arrays"""
        return self.__bin_operation__(other, __sub__)

    def __mul__(self, other: Collection) -> Collection:
        """Multiplication of two arrays"""
        return self.__bin_operation__(other, __mul__)

    def __truediv__(self, other: Collection) -> Collection:
        """self / other"""
        return self.__bin_operation__(other, __truediv__)

    def __floordiv__(self, other: Collection) -> Collection:
        """self // other"""
        return self.__bin_operation__(other, __floordiv__)

    def __mod__(self, other: Collection) -> Collection:
        """self % other"""
        return self.__bin_operation__(other, __mod__)

    def __abs__(self) -> list:
        """Returns a norm of numbers in array"""
        result = list()
        for z1 in self.to_list():
            result.append(abs(z1))
        return result

    def __pow__(self, exponent: int) -> Collection:
        """Exponentiate a array in integer exponent"""
        if not isinstance(exponent, int):
            raise TypeError("missing implementation operation"
                            "for gaussian array and %s"
                            % type(exponent).__name__)

        result = list()
        for z1 in self.to_list():
            result.append(z1 ** exponent)
        return GaussianArray(*result)

    def conjurate(self) -> Collection:
        """Returns a array of conjugated numbers"""
        result = list()
        for z1 in self.to_list():
            result.append(z1.conjugate())
        return GaussianArray(*result)

    def count(self, value: GaussianInteger) -> int:
        """Return number of occurrences of value"""
        result = 0
        for elem in self.to_list():
            if elem == value:
                result += 1
        return result

    def index(self, value: GaussianInteger) -> int:
        """
        Return first index of value\\
        If value not in array than return -1
        """
        for i in range(len(self)):
            if self.to_list()[i] == value:
                return i
        return -1

    def to_list(self) -> list:
        """Converts in a builtin list"""
        return self.__container__

    def to_tuple(self) -> tuple:
        """Converts in a builtin tuple"""
        return tuple(self.__container__)

    @staticmethod
    def zeros(n_values: int) -> Collection:
        """Returns an array of zeros values"""
        result = [gauss_zero for _ in range(n_values)]
        return GaussianArray(*result)

    @staticmethod
    def random(n_values: int, a: int, b: int,
               seed: int | None = None) -> Collection:
        """
        Returns an array of random values

        a - min value for random generation\\
        b - max value for random generation\\
        seed: int | None = None - seed for random generation
        """
        result = [GaussianInteger.random(a, b, seed) for _ in range(n_values)]
        return GaussianArray(*result)


class GaussianMatrix(Collection):
    """Represents a matrix of gaussian numbers"""
    __container__: list
    __shape__: int

    def __init__(self, *values: *Sequence[GaussianInteger]):
        pass

    def __getitem__(self, ind: int) -> GaussianInteger:
        pass

    def __setitem__(self, ind: int, value: GaussianInteger) -> None:
        pass

    def __len__(self) -> int:
        pass

    def __contains__(self, item) -> bool:
        pass

    def __iter__(self) -> Iterator[GaussianInteger]:
        pass

    def __reversed__(self) -> Iterator[GaussianInteger]:
        pass

    def __bin_operation__(self, other: Collection,
                          operation: Callable) -> Collection:
        pass

    def __add__(self, other: Collection) -> Collection:
        """Addition of two matrixes"""
        return self.__bin_operation__(other, __add__)

    def __neg__(self) -> Collection:
        """Returns negative matrix"""
        pass

    def __sub__(self, other: Collection) -> Collection:
        """Subtract of two matrixes"""
        return self.__bin_operation__(other, __sub__)

    def __mul__(self, other: Collection) -> Collection:
        """Multiplication of two matrixes"""
        return self.__bin_operation__(other, __mul__)

    def __truediv__(self, other: Collection) -> Collection:
        """self / other"""
        return self.__bin_operation__(other, __truediv__)

    def __floordiv__(self, other: Collection) -> Collection:
        """self // other"""
        return self.__bin_operation__(other, __floordiv__)

    def __mod__(self, other: Collection) -> Collection:
        """self % other"""
        return self.__bin_operation__(other, __mod__)

    def __abs__(self) -> list:
        """Returns a norm of numbers in matrix"""
        pass

    def __pow__(self, exponent: int) -> Collection:
        """Exponentiate a matrix in integer exponent"""
        pass

    def conjurate(self) -> Collection:
        """Returns a matrix of conjugated numbers"""
        pass

    def to_list(self) -> list:
        """Converts in a builtin list"""
        pass

    def to_tuple(self) -> tuple:
        """Converts in a builtin tuple"""
        pass

    @staticmethod
    def zeros(n_values: int) -> Collection:
        """Returns an matrix of zeros values"""
        pass

    @staticmethod
    def random(n_values: int, a: int, b: int,
               seed: int | None = None) -> Collection:
        """
        Returns an matrix of random values

        a - min value for random generation\\
        b - max value for random generation\\
        seed: int | None = None - seed for random generation
        """
        pass
