# DH2020

This is our project in the course Digital Humanities at Ben Gurion University under the guidance of Yael Netzer. This project is about the changing in the Hebrew language during the years thorugh the examining of song lyrics.

All the data here is for STUDY ONLY, NON-COMMERCIAL USE.

Our reasearch question is how the Hebrew language changed during the last 50 decades (1970 until today- 2020).
We examined lyrics of 90000 songs, cleaned the words using Meni Adler tagger and then counted the number of appearances of each word in every decade.

Project Website Link: https://moshehat.wixsite.com/hebrewsongs

Add_Year_To_Json.py: fetching the years the songs released at from with Spotipy library, mapping each song to a year.

Concluding_Results.py: taking the words that appear the most

Counting_Words.py: counting all the words by decades
Parsing_Kaggle_DB.py: parsing dataset from Kaggle.com

Parsing_Lyrics_DB.py: parsing dataset from lyrics.co.il

songs_to_years_json.json: dictionary with songs mapped to their years

words_appearence.json: dictionary with dictionary of decades, each contains all the word appearance times.


