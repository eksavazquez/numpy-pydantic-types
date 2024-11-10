"""Floats class for pydantic."""

from typing import TypeVar
import pydantic
from numpy import float32 as np_float32
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema, SchemaSerializer, core_schema

from .numpy_type import NumpyType

F = TypeVar("F", bound=np_float32)


class NumpyFloat(NumpyType[F]):
    """NumpyFloat class for pydantic."""

    __pydantic_serializer__ = None

    @classmethod
    def __get_pydantic_json_schema__(
        cls: type["NumpyFloat[F]"],
        schema: core_schema.CoreSchema,
        handler: pydantic.GetCoreSchemaHandler,
    ) -> JsonSchemaValue:
        """Get pydantic json schema."""
        # Define how it should look in the JSON schema
        return {
            "type": "number",
            "format": f"{cls.__name__}",
        }

    @classmethod
    def __get_pydantic_core_schema__(
        cls: type["NumpyFloat[F]"],
        source_type: type,
        handler: pydantic.GetCoreSchemaHandler,
    ) -> CoreSchema:
        """Get pydantic core schema."""
        # Define the core schema
        schema = core_schema.no_info_after_validator_function(
            cls.validate_numpy_type,
            core_schema.float_schema(
                serialization=core_schema.plain_serializer_function_ser_schema(lambda x: float(str(x)))
            ),
        )
        cls.__pydantic_serializer__ = SchemaSerializer(schema)
        return schema

    @classmethod
    def validate_numpy_type(cls: type["NumpyType[F]"], v: float) -> "NumpyType[F]":
        """Validate numpy type."""
        return cls(F(v))  # type: ignore


class float32(np_float32, NumpyFloat[np_float32]):
    """float32 class for pydantic."""
