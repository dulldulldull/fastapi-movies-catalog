from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    genre: str
    slug: str


class Movie(MovieBase):
    """
    Model of the movie
    """


class MovieCreate(MovieBase):
    """
    Model of the movie creation
    """

    title: Annotated[
        str,
        Len(min_length=3),
    ]
    description: Annotated[
        str,
        Len(min_length=3),
    ]
    genre: Annotated[
        str,
        Len(min_length=3),
    ]
    slug: Annotated[
        str,
        Len(min_length=3),
    ]
