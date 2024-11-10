# numpy-pydantic-types
**numpy-pydantic-types** is a Python library providing `numpy` scalar data types compatible with `pydantic`, allowing for easy validation and enforcement of numerical precision in `pydantic` models.

## Overview
`pydantic` models rely on Python's native types (e.g., `int`, `float`, `str`) for data validation, which can be limiting when working with scientific or numerical applications that require specific `numpy` types, like `float32`, `uint16`, or `int8`. This library bridges that gap by introducing numpy scalar types as valid pydantic field types, allowing you to define precise, controlled models that integrate with scientific workflows.

## Features
- **Numpy Scalar Compatibility**: Define `pydantic` models using `numpy` scalar types like `float32`, `uint32`, `int8`, etc.
- **Strict Type Enforcement**: Ensures model fields adhere to specific precision and range constraints.
- **Simple Integration**: Easily import and use `numpy` types in your `pydantic` models.
## Installation
```
pip install numpy-pydantic-types
```

# Usage
This library enables the use of `numpy` scalar types directly within `pydantic` models. Here’s how to set up a model using `numpy` types:

```
from pydantic import BaseModel, ValidationError
from numpy_pydantic_types import Float32, UInt32, UInt16

class ScientificModel(BaseModel):
    precision_value: Float32  # Enforces a 32-bit floating point
    sample_count: UInt32  # Enforces a 32-bit unsigned integer
    sensor_id: UInt16  # Enforces a 16-bit unsigned integer

# Example data
data = {
    "precision_value": 1.234567,
    "sample_count": 4294967295,  # Max value for UInt32
    "sensor_id": 65535  # Max value for UInt16
}

# Instantiate the model with the specific numpy types
try:
    model = ScientificModel(**data)
    print("Model validated successfully:", model)
except ValidationError as e:
    print("Validation error:", e)
```

## Supported Numpy Types
The library provides a range of `numpy` scalar types that can be used in `pydantic` models, including:

- **Float Types**: `Float32`, `Float64`
- **Signed Integer Types**: `Int8`, `Int16`, `Int32`, `Int64`
- **Unsigned Integer Types**: `UInt8`, `UInt16`, `UInt32`, `UInt64`
## Example Model
Using specific `numpy` scalar types can help enforce type constraints in applications where precision or memory footprint is crucial, such as scientific computations, data analysis, or embedded systems.

```
from numpy_pydantic_types import Int8, Float64

class DataProcessingModel(BaseModel):
    temperature: Float64
    adjustment_factor: Int8
```

## Why Use Numpy Scalar Types?
- **Precision**: Control over numerical precision, essential in scientific or numerical applications.
- **Range Enforcement**: Ensures values conform to specific data type ranges (e.g., `UInt8` ranges from 0 to 255).
- **Memory Efficiency**: Helps reduce memory consumption by enforcing smaller data types.

## License
MIT License
