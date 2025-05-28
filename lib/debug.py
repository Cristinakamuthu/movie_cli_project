from lib.helper import get_all_movies, find_movie_by_id, create_movie

movies = get_all_movies()
for movie in movies:
    print(movie.title)

new_movie = create_movie('The Devs Return', 2026, 1, 2)
print(new_movie.title)

movie = find_movie_by_id(1)
print(movie.title)
