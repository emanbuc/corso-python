current_movies={"The Matrix": "2023-10-01 20:00",
                 "Inception": "2023-10-02 21:00"}
print("Current Movie Schedule:")

for key in current_movies:
    print(key)

movie=input("Enter the movie name to check its schedule: ")

showtime=current_movies.get(movie, "Movie not found in schedule")
print(f"Showtime for {movie}: {showtime}")
