import pytest
from _init_ import add_movie

@pytest.fixture
def new_movie(movie):
    movie = add_movie(name="Star Wars:Nova nadeje",
                                 director="George Lucas",
                                 year=1977,
                                 genre="scifi")
    return movie

def test_addmovie(new_movie):
    assert type(new_movie.name) is str