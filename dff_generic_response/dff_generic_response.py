"""Main module"""
from typing import Any, Dict, Optional, List, Union

from pydantic import Extra, BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        extra = Extra.allow


class Command(BaseModel):
    command: str = ...


class Audio(BaseModel):
    url: str = ...
    title: Optional[str] = None


class Video(BaseModel):
    url: str = ...
    title: Optional[str] = None


class Image(BaseModel):
    url: str = ...
    title: Optional[str] = None


class Gallery(BaseModel):
    images: List[Image] = ...


class Attachment(BaseModel):
    url: str = ...
    title: Optional[str] = None


class Link(BaseModel):
    url: str = ...
    title: Optional[str] = None

    def html(self):
        return f'<a href="{self.url}">{self.title if self.title else self.url}</a>'


class Button(BaseModel):
    title: str = ...
    url: Optional[str] = None
    payload: Optional[dict] = None


class Keyboard(BaseModel):
    """
    Class :py:class:`~Keyboard` describes a set of buttons that remains available to the user during all turns
    or during several turns.
    """

    buttons: List[Button]


class Markup(BaseModel):
    """
    Class :py:class:`~Markup` is meant to describe inline keyboards that get hidden after the user has responded.
    Like :py:class:`~Keyboard`, it contains a list of buttons.
    """

    buttons: List[Button]


class GenericResponse(BaseModel):
    text: str = ...
    keyboard: Optional[Keyboard] = None
    markup: Optional[Markup] = None
    attachment: Optional[Attachment] = None
    image: Optional[Image] = None
    gallery: Optional[Gallery] = None
    video: Optional[Video] = None
    audio: Optional[Audio] = None
    commands: Optional[List[Command]] = None
    end_session: Optional[bool] = False


__all__ = [
    "Command",
    "Audio",
    "Video",
    "Image",
    "Attachment",
    "Link",
    "Button",
    "Keyboard",
    "Markup",
    "GenericResponse",
]
