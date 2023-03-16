class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = 0
        self.rating_counter = 0
        self.serie_rating = 0

    def __str__(self):
        genre_string = ", ".join(self.genres)

        if self.rating_counter==0:
            rating_string = "no ratings"
        else:
            rating_string = f"{self.rating_counter} ratings, average {self.serie_rating:.1f} points"

        return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{rating_string}"

    def rate(self, rating: int):
        if 0<=rating<=5:
            self.ratings += rating
            self.rating_counter += 1
            self.serie_rating = self.ratings/self.rating_counter

def minimum_grade(rating: float, series_list: list):
    my_list = []

    for serie in series_list:
        if serie.serie_rating>=rating:
            my_list.append(serie)
    
    return my_list

def includes_genre(genre: str, series_list: list):
    my_list = []

    for serie in series_list:
        if genre in serie.genres:
            my_list.append(serie)
    
    return my_list

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)