from typing import Generic, TypeVar
from abc import ABC, abstractmethod

import pydantic
from pydantic_core import CoreSchema, core_schema
from pydantic.json_schema import JsonSchemaValue

T = TypeVar("T")


class NumpyType(Generic[T], ABC):
    """Numpy type.

    Abstract base class for all numpy types.
    """

    @classmethod
    @abstractmethod
    def __get_pydantic_json_schema__(
        cls: type["NumpyType[T]"],
        schema: core_schema.CoreSchema,
        handler: pydantic.GetCoreSchemaHandler,
    ) -> JsonSchemaValue:
        """Get pydantic json schema."""

    @classmethod
    @abstractmethod
    def __get_pydantic_core_schema__(
        cls: type["NumpyType[T]"],
        source_type: type,
        handler: pydantic.GetCoreSchemaHandler,
    ) -> CoreSchema:
        """Get pydantic core schema."""

    @classmethod
    @abstractmethod
    def validate_numpy_type(cls: type["NumpyType[T]"], v: float) -> "NumpyType[T]":
        """Validate numpy type."""
