The database of the favorite movies. User should be able to add or remove the movies and search them by categires.

# Example usage:
add_movie("Inception", "Christopher Nolan", 2010, "Science Fiction")
add_movie("The Matrix", "Wachowski Sisters", 1999, "Science Fiction")
view_movies()
edit_movie(1, new_title="Inception: The Dream")
delete_movie(2)
view_movies()
search_movie_by_title("Inception")
search_movie_by_director("Christopher Nolen")
search_movie_by_genre("Science Fiction")