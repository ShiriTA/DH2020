import codecs
import json
import glob
import re


class Counting:

    def __init__(self):
        self.word_appear = {'1970s': dict(), '1980s': dict(), '1990s': dict(), '2000s': dict(), '2010s': dict()}
        self.most_common_words()
        self.songs_count = {'1970s': dict(), '1980s': dict(), '1990s': dict(), '2000s': dict(), '2010s': dict()}

    def collect_words(self, decade, word, artist_name, track_name):
        if word not in self.word_appear[decade].keys():
            self.word_appear[decade][word] = []
        if artist_name + "-" + track_name not in self.word_appear[decade][word]:
            self.word_appear[decade][word].append(artist_name + "-" + track_name)

    def clean_word(self, word):
        if " " in word:
            word = word.split(" ")[0]
        if "^" in word:
            word = word.split("^")[1]
        if "\n" in word:
            word = word.split("\n")[0]
        if "\r" in word:
            word = word.split("\r")[0]
        if "..." in word:
            word = word.split("...")[0]
        return word

    def add_words(self, year, word, artist_name, track_name):
        if year == '197':
            self.collect_words('1970s', word, artist_name, track_name)
        if year == '198':
            self.collect_words('1980s', word, artist_name, track_name)
        if year == '199':
            self.collect_words('1990s', word, artist_name, track_name)
        if year == '200':
            self.collect_words('2000s', word, artist_name, track_name)
        if year == '201':
            self.collect_words('2010s', word, artist_name, track_name)

    def most_common_words(self):
        filenames = glob.glob("lyrics_tagged/*.txt")
        for filename in filenames:
            try:
                with codecs.open(filename, "r","utf8") as f:
                    length = len(filename.split("_"))
                    artist_name = filename.split("_")[1].split("\\")[1] + " " + filename.split("_")[2]
                    track_name = ' '.join(filename.split("_")[3:length - 2])
                    lines = f.readlines()
                    for line in lines:
                        if "year" in line:
                            year = line[6:9]
                    for line in lines:
                        if "Lemma" in line:
                            word = self.clean_word(line[8:len(line)])
                            if re.search('[a-zA-Z]', word) == None:
                                self.add_words(year, word, artist_name, track_name)
            except:
                continue

counting = Counting()
for key in counting.word_appear['1970s'].keys():
    counting.songs_count['1970s'][key] = len(counting.word_appear['1970s'][key])
for key in counting.word_appear['1980s'].keys():
    counting.songs_count['1980s'][key] = len(counting.word_appear['1980s'][key])
for key in counting.word_appear['1990s'].keys():
    counting.songs_count['1990s'][key] = len(counting.word_appear['1990s'][key])
for key in counting.word_appear['2000s'].keys():
    counting.songs_count['2000s'][key] = len(counting.word_appear['2000s'][key])
for key in counting.word_appear['2010s'].keys():
    counting.songs_count['2010s'][key] = len(counting.word_appear['2010s'][key])
with codecs.open("words_appearence_songs_count.json", "w", "utf8") as word_appearance:
    word_appearance.write(json.dumps(counting.songs_count, ensure_ascii=False))
