import codecs
import csv
import json


class Parsing():

    def __init__(self, dict_reader):
        self.most_common_dict = dict()
        self.songs_count = dict()
        self.dict_reader = dict_reader

    def collect_words(self, curr_dict, artist_name, track_name):
        for i in range(1, 13):
            lyrics_words = curr_dict['LYRICS' + str(i)].split(' ')
            for i in range(0, len(lyrics_words)):
                word = lyrics_words[i]
                if word not in self.most_common_dict.keys():
                    self.most_common_dict[word] = []
                if artist_name + "-" + track_name not in self.most_common_dict[word]:
                    self.most_common_dict[word].append(artist_name + "-" + track_name)

    def most_common_words(self):
        for curr_dict in self.dict_reader:
            if curr_dict['DECADES'] == '1980s':
                self.collect_words(curr_dict, curr_dict['PERFORMER'], curr_dict['SONG'])

    def slang(self):
        pass


with codecs.open("1001dataset.csv", "r", "utf8") as dataset:
    dict_reader = csv.DictReader(dataset)
    parsing = Parsing(dict_reader)
    parsing.most_common_words()
    for key in parsing.most_common_dict.keys():
        parsing.songs_count[key] = len(parsing.most_common_dict[key])
    with codecs.open("words_appearence_songs_count_80s.json", "w", "utf8") as word_appearance:
        word_appearance.write(json.dumps(parsing.songs_count, ensure_ascii=False))







