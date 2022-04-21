"""Main module"""
import os
from typing import Dict, Optional, List, Union
from enum import Enum

from pydantic import Extra, FilePath, HttpUrl, BaseModel as PydanticBaseModel


class Session(Enum):
    ACTIVE = 0
    FINISHED = 1


class BaseModel(PydanticBaseModel):
    class Config:
        extra = Extra.allow


class Command(BaseModel):
    command: str = ...


class Resource(BaseModel):
    source: Union[HttpUrl, FilePath] = ...
    title: Optional[str] = None


class Audio(Resource):
    pass


class Video(Resource):
    pass


class Image(Resource):
    pass


class Document(Resource):
    pass


class Attachments(BaseModel):
    files: List[Resource] = ...


class Link(Resource):
    @property
    def html(self):
        return f'<a href="{self.source}">{self.text if self.text else self.source}</a>'


class Button(BaseModel):
    source: Optional[str] = None
    text: str = ...
    payload: Optional[dict] = None


class Keyboard(BaseModel):
    buttons: List[Button] = ...


class Response(BaseModel):
    text: str = ...
    ui: Optional[Union[Keyboard, BaseModel]] = None
    document: Optional[Document] = None
    image: Optional[Image] = None
    gallery: Optional[Attachments] = None
    video: Optional[Video] = None
    audio: Optional[Audio] = None
    commands: Optional[List[Command]] = None
    state: Optional[Session] = Session.ACTIVE


__all__ = [
    "Command",
    "Attachments",
    "Audio",
    "Video",
    "Image",
    "Document",
    "Link",
    "Button",
    "Keyboard",
    "Response",
]
