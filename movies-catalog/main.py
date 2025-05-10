from typing import Annotated

from fastapi import (
    FastAPI,
    Request,
    Depends,
    HTTPException,
    status,
)

from schemas.movie import Movie

app = FastAPI(
    title="Movies Catalog",
)


@app.get("/")
def read_root(
    request: Request,
    name: str = "World",
):
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "message": f"Hello {name}",
        "docs": str(docs_url),
    }


MOVIES = [
    Movie(
        movie_id=1,
        title="Movie 1",
        description="Movie 1 description",
        genre="Comedy",
    ),
    Movie(
        movie_id=2,
        title="Movie 2",
        description="Movie 2 description",
        genre="Drama",
    ),
    Movie(
        movie_id=3,
        title="Movie 3",
        description="Movie 3 description",
        genre="Animation",
    ),
]


@app.get(
    "/movies",
    response_model=list[Movie],
)
def read_all_movies():
    return MOVIES


def prefetch_movie(
    movie_id: int,
) -> Movie:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.movie_id == movie_id),
        None,
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie id {movie_id!r} not found",
    )


@app.get(
    "/movies/{movie_id}/",
    response_model=Movie,
)
def read_one_movie(
    movie: Annotated[
        Movie,
        Depends(prefetch_movie),
    ],
) -> Movie:
    return movie
