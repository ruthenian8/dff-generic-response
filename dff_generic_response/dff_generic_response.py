"""Main module"""
from typing import Any, Dict, Optional, List, Union

from pydantic import BaseModel, Field


class Link(BaseModel):
    url: str = ...
    title: Optional[str] = url
    hide: bool = False

    def html(self):
        return f'<a href="{self.url}">{self.title if self.title else self.url}</a>'


class GenericResponse(BaseModel):
    # required by: TG, Alice, FB
    text: str = ...
    buttons: Optional[List[Union[str, BaseModel]]]
    links: Optional[List[BaseModel]]
    attachment: Optional[str]
    end_session: Optional[bool]
    # required by: TG, Alice
    audio_url: Optional[str]
    image_url: Optional[str]

    misc_options: Optional[Union[Dict[str, Any], BaseModel]]

    def __init__(
        self,
        *,
        text: str,
        buttons: Optional[List[Union[str, BaseModel]]] = Field(default_factory=list),
        links: Optional[List[BaseModel]] = Field(default_factory=list),
        attachment: Optional[str] = None,
        end_session: Optional[bool] = False,
        audio_url: Optional[str] = None,
        image_url: Optional[str] = None,
        misc_options: Optional[Union[Dict[str, Any], BaseModel]] = None,
        **kwargs
    ):
        if not misc_options:
            misc_options = kwargs
        
        locals().pop("kwargs")

        super().__init__(**locals())
