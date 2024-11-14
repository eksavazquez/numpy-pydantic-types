from types import new_class
from typing import TYPE_CHECKING
from numpy import float16 as np_float16
from numpy import float32 as np_float32
from numpy import float64 as np_float64

from .floats import NumpyFloat  # Adjust import path as needed

__all__ = ["float16", "float32", "float64"]

if TYPE_CHECKING:

    class float16(np_float16, NumpyFloat[np_float16]): ...

    class float32(np_float32, NumpyFloat[np_float32]): ...

    class float64(np_float32, NumpyFloat[np_float64]): ...


# Dynamically create each float class at runtime
for name, np_type in [
    ("float16", np_float16),
    ("float32", np_float32),
    ("float64", np_float64),
]:
    new_class_type = new_class(
        name,
        (np_type, NumpyFloat[np_type]),  # type: ignore[valid-type]
        exec_body=lambda ns: ns.update({"__doc__": f"{name} class for pydantic."}),
    )
    globals()[name] = new_class_type
