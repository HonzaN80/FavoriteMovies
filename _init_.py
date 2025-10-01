import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
   level=logging.INFO,
   format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
   datefmt="%d-%b-%y %H:%M:%S")

logger.debug("This is debug")
logger.info("This is info")
logger.warning("This is warning")
logger.error("This is error")

movies = []

# Function to add a new movie
def add_movie(name, director, year, genre):
    try:
        # Each movie is represented as a dictionary
        movie = {
            "id": len(movies) + 1,  # Unique ID for the movie
            "name": name,
            "director": director,
            "year": int(year),
            "genre": genre
        }
        movies.append(movie)  # Add the movie to the list
        print(f"Movie '{name}' added successfully.")
    except ValueError:
        print("Year must be set as a number.")

def edit_movie(movie_name, new_name=None, new_director=None, new_year=None, new_genre=None):
    found = False
    for movie in movies:
        if movie["name"] == movie_name:
            found = True
            if new_name:
                movie["name"] = new_name
            if new_director:
                movie["director"] = new_director
            if new_year:
                try:
                    movie["year"] = int(new_year)
                except ValueError:
                    print("New year must be a number.")
            if new_genre:
                movie["genre"] = new_genre
            print(f"Movie '{movie_name}' updated successfully.")
            break
    if not found:
        print(f"Movie '{movie_name}' not found.")

def view_movies():
    if movies:
        for movie in movies:
            print(f"{movie['id']}. {movie['name']}, directed by {movie['director']}, "
                  f"released in {movie['year']}, Genre: {movie['genre']}")
    else:
        print("No movies in the database.")

def search_movie_by_name(name):
    found_movies = [movie for movie in movies if name.lower() in movie["name"].lower()]
    if found_movies:
        for movie in found_movies:
            print(f"{movie['id']}. {movie['name']}, directed by {movie['director']}, "
                  f"released in {movie['year']}, Genre: {movie['genre']}")
    else:
        print(f"No movies found with title '{name}'.")

def search_movie_by_director(director):
    found_movies = [movie for movie in movies if director.lower() in movie["director"].lower()]
    if found_movies:
        for movie in found_movies:
            print(f"{movie['id']}. {movie['name']}, directed by {movie['director']}, "
                  f"released in {movie['year']}, Genre: {movie['genre']}")
    else:
        print(f"No movies found directed by '{director}'.")

def search_movie_by_genre(genre):
    found_movies = [movie for movie in movies if genre.lower() in movie["genre"].lower()]
    if found_movies:
        for movie in found_movies:
            print(f"{movie['id']}. {movie['name']}, directed by {movie['director']}, "
                  f"released in {movie['year']}, Genre: {movie['genre']}")
    else:
        print(f"No movies found in genre '{genre}'.")

def delete_movie(movie_id):
    global movies
    initial_count = len(movies)
    movies = [movie for movie in movies if movie["id"] != movie_id]
    if len(movies) < initial_count:
        print(f"Movie with ID {movie_id} deleted successfully.")
    else:
        print(f"No movie found with ID {movie_id}.")

