from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Dummy(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class Complex(_message.Message):
    __slots__ = ("dummy", "dummies")
    DUMMY_FIELD_NUMBER: _ClassVar[int]
    DUMMIES_FIELD_NUMBER: _ClassVar[int]
    dummy: Dummy
    dummies: _containers.RepeatedCompositeFieldContainer[Dummy]
    def __init__(self, dummy: _Optional[_Union[Dummy, _Mapping]] = ..., dummies: _Optional[_Iterable[_Union[Dummy, _Mapping]]] = ...) -> None: ...
