from .floats import NumpyFloat

from numpy import float16 as np_float16
from numpy import float32 as np_float32
from numpy import float64 as np_float64

class float16(np_float16, NumpyFloat[np_float16]): ...
class float32(np_float32, NumpyFloat[np_float32]): ...
class float64(np_float32, NumpyFloat[np_float64]): ...

__all__ = ["float16", "float32", "float64"]
