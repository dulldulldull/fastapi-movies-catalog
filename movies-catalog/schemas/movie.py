from typing import Annotated

from annotated_types import Len
from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str
    description: str
    genre: str


class Movie(MovieBase):
    """
    Model of the movie
    """

    movie_id: int


class MovieCreate(MovieBase):
    """
    Model of the movie creation
    """

    title: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
    description: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
    genre: Annotated[
        str,
        Len(min_length=3, max_length=10),
    ]
