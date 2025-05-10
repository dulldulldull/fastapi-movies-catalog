from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_id: int
    title: str
    description: str
    genre: str


class Movie(MovieBase):
    """
    Model of the movie
    """
