#!/usr/bin/python
# -*- coding: utf-8 -*-
# imports the class from the media.py file we created
# imports fresh_tomatoes.py for content

import fresh_tomatoes
import media

#We store movies using the class Movie inside media.py, the file we imported.
#The Class Movie uses a Constructor that takes several Instance Variables.
#Each of the movies are therefore considered Instances, the details Variables.

toy_story = media.Movie('Toy Story',
                        'A story of a boy and his toys that come to life'
                        ,
                        'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg'
                        , 'https://www.youtube.com/watch?v=vwyZH85NQC4')

avatar = media.Movie('Avatar', 'A marine on an alien planet',
                     'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg'
                     , 'https://www.youtube.com/watch?v=5PSNL1qE6VY')

train_to_busan = media.Movie('Train to Busan',
                             'A zombie apocalypse escaped by train',
                             'https://upload.wikimedia.org/wikipedia/en/9/95/Train_to_Busan.jpg'
                             ,
                             'https://www.youtube.com/watch?v=E2nrE9JnaDg'
                             )

worldwarz = media.Movie('World War Z', 'A zombie apocalypse contagion',
                        'https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg'
                        , 'https://www.youtube.com/watch?v=HcwTxRuq-uk')

the_matrix = media.Movie('The Matrix', 'A sci-fi film thats crazy',
                         'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg'
                         , 'https://www.youtube.com/watch?v=m8e-FF8MsqU'
                         )

resident_evil = media.Movie('Resident Evil', 'The first of the releases'
                            ,
                            'https://upload.wikimedia.org/wikipedia/en/a/a1/Resident_evil_ver4.jpg'
                            ,
                            'https://www.youtube.com/watch?v=jiS6gtClrqk'
                            )

movies = [
    toy_story,
    avatar,
    train_to_busan,
    worldwarz,
    the_matrix,
    resident_evil,
    ]

fresh_tomatoes.open_movies_page(movies)
#print media.Movie.VALID_RATINGS
#print media.Movie.__module__
