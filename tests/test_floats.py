from typing import Any, TypeVar
from numpy import floating
from pydantic import BaseModel
import pytest
from numpy_pydantic_types import float16, float32, float64

F = TypeVar("F", bound=floating[Any])

float_types = [float16, float32, float64]


@pytest.mark.parametrize("float_type", float_types)
def test_floats_hash(float_type: type[F]) -> None:
    """Test floats hash."""
    assert hash(float_type(0.02)) == hash(float_type(0.02))
    assert hash(float_type(99.9)) != hash(float_type(100.0))


# Test pydantic models


class DataProcessingModel(BaseModel):
    temperature: float32


def test_model_json_schema() -> None:
    """Test model json schema."""
    assert DataProcessingModel.model_json_schema() == {
        "properties": {
            "temperature": {
                "format": "float32",
                "title": "Temperature",
                "type": "number",
            }
        },
        "required": ["temperature"],
        "title": "DataProcessingModel",
        "type": "object",
    }
