"""Main module"""
from typing import Optional, List, Union
from enum import Enum

from pydantic import BaseModel, Field


class YandexCommands(Enum):
    EXIT = "exit"
    REQUEST_GEOLOCATION = "request_geolocation"


class Link(BaseModel):
    title: Optional[str] = None
    url: str = ...
    hide: bool = False

    def html(self):
        return f'<a href="{self.url}">{self.title if self.title else self.url}</a>'


class GenericResponse(BaseModel):
    # required by: TG, Alice, FB
    text: str = ...
    buttons: Optional[List[Union[str, BaseModel]]] = Field(default_factory=list)
    links: Optional[List[BaseModel]] = Field(default_factory=list)
    # required by: TG, Alice
    audio_url: Optional[str] = None
    image_url: Optional[str] = None
    # required by: Alice
    image: Optional[bytes] = None
    gallery: Optional[BaseModel] = None
    image_id: Optional[str] = None
    tts: Optional[str] = text  # goes to Alice's tts response section
    commands: Optional[List[str]] = Field(default_factory=list)
    directives: Optional[dict] = None
    show_item_meta: Optional[BaseModel] = None
    should_listen: Optional[bool] = None
    end_session: Optional[bool] = None

    def __init__(self, **kwargs):
        commands = kwargs.get("commands", [])
        if YandexCommands.EXIT or "exit" in commands:
            kwargs["end_session"] = True

        super().__init__(**kwargs)
