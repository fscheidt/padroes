from typing import (
    Annotated,
    Any,
    BinaryIO,
    TypeVar,
    cast,
)

from annotated_doc import Doc
from starlette.datastructures import Headers as Headers  # noqa: F401
from starlette.datastructures import UploadFile as StarletteUploadFile

class UploadFile(StarletteUploadFile):
    """
    A file uploaded in a request.
    """
    file: Annotated[
        BinaryIO,
        Doc("The standard Python file object (non-async)."),
    ]
    filename: Annotated[str | None, Doc("The original file name.")]
    size: Annotated[int | None, Doc("The size of the file in bytes.")]
    headers: Annotated[Headers, Doc("The headers of the request.")]
    content_type: Annotated[
        str | None, Doc("The content type of the request, from the headers.")
    ]
    async def write(
        self,
        data: Annotated[
            bytes,
            Doc(""" The bytes to write to the file."""),
        ],
    ) -> None:
        return await super().write(data)

    @classmethod
    def _validate(cls, __input_value: Any, _: Any) -> "UploadFile":
        if not isinstance(__input_value, StarletteUploadFile):
            raise ValueError(f"Expected UploadFile, received: {type(__input_value)}")
        return cast(UploadFile, __input_value)

class DefaultPlaceholder:

    def __init__(self, value: Any):
        self.value = value

    def __bool__(self) -> bool:
        return bool(self.value)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, DefaultPlaceholder) and o.value == self.value

DefaultType = TypeVar("DefaultType")

def Default(value: DefaultType) -> DefaultType:
    return DefaultPlaceholder(value)
