""" Module responsible for feeding and call movies page. """
import media
import fresh_tomatoes


toy_story = media.Movie('Toy Story',
                        'http://www.gstatic.com/tv/thumb/movieposters/17420'
                        '/p17420_p_v8_ab.jpg',
                        'https://www.youtube.com/watch?v=tN1A2mVnrOM')

totoro = media.Movie('Tonari no Totoro',
                     'https://upload.wikimedia.org/'
                     'wikipedia/pt/8/88/Meu_Vizinho_Totoro_-_'
                     'Tonari_no_Totoro_%28poster_japones%29.jpg',
                     'https://www.youtube.com/watch?v=92a7Hj0ijLs')

last_samurai = media.Movie('Last Samurai',
                           'https://upload.wikimedia.org/'
                           'wikipedia/en/c/c6/The_Last_Samurai.jpg',
                           'https://www.youtube.com/watch?v=T50_qHEOahQ')

harry_potter = media.Movie('Harry Potter and the Pilosopher\'s Stone',
                           'https://vignette3.wikia.nocookie.net/'
                           'harrypotter/images/0/0e/Philostone.jpg/'
                           'revision/latest?cb=20101208171110',
                           'https://www.youtube.com/watch?v=VyHV0BRtdxo')

# Add movies to array
movies = [toy_story, totoro, last_samurai, harry_potter]

# Call open_movies_page using movies array
fresh_tomatoes.open_movies_page(movies)
