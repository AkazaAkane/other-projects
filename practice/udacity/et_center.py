import fresh_tomatoes
import media

weathering_with_you = media.Movie("Weathering with You",
                                "NA",
                                "https://upload.wikimedia.org/wikipedia/zh/4/44/Tenki_no_ko_Key_Visual.jpg",
                                "https://www.youtube.com/watch?v=Q6iK6DjV_iE")
#weathering_with_you.show_trailer()

movies = [weathering_with_you]
fresh_tomatoes.open_movies_page(movies)
