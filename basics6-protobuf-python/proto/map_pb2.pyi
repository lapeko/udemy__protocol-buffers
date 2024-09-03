from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TestMap(_message.Message):
    __slots__ = ("key_value_map",)
    class KeyValueMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    KEY_VALUE_MAP_FIELD_NUMBER: _ClassVar[int]
    key_value_map: _containers.ScalarMap[int, str]
    def __init__(self, key_value_map: _Optional[_Mapping[int, str]] = ...) -> None: ...
