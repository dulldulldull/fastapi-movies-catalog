from pydantic import BaseModel

from schemas.movie import Movie, MovieCreate


class MoviesStorage(BaseModel):
    slug_to_movie: dict[str, Movie] = {}

    def get(self) -> list[Movie]:
        return list(self.slug_to_movie.values())

    def get_by_slug(self, slug: str) -> Movie | None:
        return self.slug_to_movie.get(slug)

    def create(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(
            **movie_in.model_dump(),
        )
        self.slug_to_movie[movie.slug] = movie
        return movie

    def delete_by_slug(self, slug: str) -> None:
        self.slug_to_movie.pop(slug, None)

    def delete(self, movie: Movie) -> None:
        self.delete_by_slug(slug=movie.slug)


storage = MoviesStorage()

storage.create(
    MovieCreate(
        slug="movie-1",
        title="Movie 1",
        description="Movie 1 description",
        genre="Comedy",
    )
)

storage.create(
    MovieCreate(
        slug="movie-2",
        title="Movie 2",
        description="Movie 2 description",
        genre="Drama",
    )
)

storage.create(
    MovieCreate(
        slug="movie-3",
        title="Movie 3",
        description="Movie 3 description",
        genre="Animation",
    )
)
