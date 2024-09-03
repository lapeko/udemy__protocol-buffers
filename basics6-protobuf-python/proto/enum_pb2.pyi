from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EYE_COLOR(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EYE_COLOR_UNSPECIFIED: _ClassVar[EYE_COLOR]
    EYE_COLOR_BLUE: _ClassVar[EYE_COLOR]
    EYE_COLOR_GREEN: _ClassVar[EYE_COLOR]
EYE_COLOR_UNSPECIFIED: EYE_COLOR
EYE_COLOR_BLUE: EYE_COLOR
EYE_COLOR_GREEN: EYE_COLOR

class EyeColor(_message.Message):
    __slots__ = ("eye_color",)
    EYE_COLOR_FIELD_NUMBER: _ClassVar[int]
    eye_color: EYE_COLOR
    def __init__(self, eye_color: _Optional[_Union[EYE_COLOR, str]] = ...) -> None: ...
