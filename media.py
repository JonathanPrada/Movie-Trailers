#!/usr/bin/python
# -*- coding: utf-8 -*-
import webbrowser

#Class movie takes in Instance variables using the constructor def __init__
class Movie:

    """ This class provides a way to store movie related information """

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(
        self,
        movie_title,
        movie_storyline,
        poster_image,
        trailer_youtube,
        ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#Instance method opens the youtube url using the provided variables
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



			
