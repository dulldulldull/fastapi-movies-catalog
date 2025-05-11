from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
    Form,
)

from .dependencies import (
    prefetch_movie,
)
from .crud import MOVIES

import random

from schemas.movie import Movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[Movie],
)
def read_all_movies():
    return MOVIES


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    genre: Annotated[str, Form()],
):
    movie_id = random.randint(0, 1000)
    return Movie(
        movie_id=movie_id,
        title=title,
        description=description,
        genre=genre,
    )


@router.get(
    "/{movie_id}/",
    response_model=Movie,
)
def read_one_movie(
    movie: Annotated[
        Movie,
        Depends(prefetch_movie),
    ],
) -> Movie:
    return movie
