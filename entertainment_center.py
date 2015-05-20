import media
import fresh_tomatoes

# define the movies
toy_story = media.Movie("Toy Story",
                        "The secret life of toys when people are not around." ,
                        "http://upload.wikimedia.org/wikipedia/en/1/13/"
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

school_of_rock = media.Movie("School of Rock",
                             "The story of a depressed rocker and his private"
                             "school band",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/"
                             "School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille =  media.Movie("Ratatouille",
                           "A rat who can cook makes an unusual alliance with"
                           " a young kitchen worker at a famous restaurant.",
                           "http://upload.wikimedia.org/wikipedia/en/5/50/"
                           "RatatouillePoster.jpg",
                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")


# use fresh_tomatoes to build page
movies = [toy_story, school_of_rock, ratatouille]
fresh_tomatoes.open_movies_page(movies)


