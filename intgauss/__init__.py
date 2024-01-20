from ._base import GaussianInteger
from ._primes import *
from ._funcs import *
from ._arrays import *


gauss_units = (
    GaussianInteger(1, 0),
    GaussianInteger(-1, 0),
    GaussianInteger(0, 1),
    GaussianInteger(0, -1)
)

gauss_zero = GaussianInteger(0, 0)
