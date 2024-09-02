from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Simple(_message.Message):
    __slots__ = ("id", "is_simple", "name", "numbers")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_SIMPLE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    id: int
    is_simple: bool
    name: str
    numbers: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., is_simple: bool = ..., name: _Optional[str] = ..., numbers: _Optional[_Iterable[int]] = ...) -> None: ...
