from pydantic import BaseModel
from numpy_pydantic_types import float32


def test_float32_hash() -> None:
    """Test float32 hash."""
    assert hash(float32(0.02)) == hash(float32(0.02))
    assert hash(float32(99.9)) != hash(float32(100.0))


# Test pydantic models


class DataProcessingModel(BaseModel):
    temperature: float32


def test_model_json_schema() -> None:
    """Test model json schema."""
    assert DataProcessingModel.model_json_schema() == {
        "properties": {"temperature": {"format": "float32", "title": "Temperature", "type": "number"}},
        "required": ["temperature"],
        "title": "DataProcessingModel",
        "type": "object",
    }
