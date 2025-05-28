from lib.helper import get_all_movies, get_all_actors, get_all_directors, find_movie_by_id, create_movie

def menu():
    print("🎬 Welcome to the Movie App 🎬")
    print("1. View all movies")
    print("2. View all actors")
    print("3. View all directors")
    print("4. Find movie by ID")
    print("5. Create a new movie")
    print("6. Exit")

def run():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == "1":
            movies = get_all_movies()
            for movie in movies:
                print(f"{movie.id}. {movie.title} ({movie.release_year})")

        elif choice == "2":
            actors = get_all_actors()
            for actor in actors:
                print(f"{actor.id}. {actor.name} - Age: {actor.age}")

        elif choice == "3":
            directors = get_all_directors()
            for director in directors:
                print(f"{director.id}. {director.name} - Style: {director.style}")

        elif choice == "4":
            id = input("Enter movie ID: ")
            movie = find_movie_by_id(id)
            if movie:
                print(f"{movie.title} ({movie.release_year})")
                print(f"Director: {movie.director.name}")
                print(f"Main Actor: {movie.main_actor.name}")
            else:
                print("Movie not found.")

        elif choice == "5":
            title = input("Title: ")
            year = input("Release Year: ")
            director_id = input("Director ID: ")
            actor_id = input("Main Actor ID: ")
            movie = create_movie(title, year, director_id, actor_id)
            print(f"{movie.title} was created successfully!")

        elif choice == "6":
            print("Goodbye 🎥")
            break

        else:
            print("Invalid choice. Try again.")
