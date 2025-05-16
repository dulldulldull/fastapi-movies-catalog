from typing import Annotated

from fastapi import (
    Depends,
    APIRouter,
    status,
)

from .dependencies import (
    prefetch_movie,
)
from .crud import MOVIES

import random

from schemas.movie import Movie, MovieCreate

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
    movie_create: MovieCreate,
):
    movie_id = random.randint(0, 1000)
    return Movie(
        movie_id=movie_id,
        **movie_create.model_dump(),
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
