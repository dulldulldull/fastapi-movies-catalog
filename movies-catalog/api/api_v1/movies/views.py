from typing import Annotated

from fastapi import Depends, APIRouter

from .dependencies import (
    prefetch_movie,
)
from .crud import MOVIES

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
