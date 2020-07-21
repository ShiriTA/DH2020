import codecs
import json
import glob
import re


class Counting:

    def __init__(self):
        self.word_appear = {'1970s': dict(), '1980s': dict(), '1990s': dict(), '2000s': dict(), '2010s': dict()}
        self.most_common_words()
        self.to_filter = ["את", "כל", "רק", "עם", "יש", "הוא", "היא", "אני", "הם", "הן", "אנחנו", "אתם","לא","כן","אתן"]

    def collect_words(self, decade, word):
        if word in self.word_appear[decade].keys():
            self.word_appear[decade][word] += 1
        else:
            self.word_appear[decade][word] = 1

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

    def add_words(self, year, word):
        if year == '197':
            self.collect_words('1970s', word)
        if year == '198':
            self.collect_words('1980s', word)
        if year == '199':
            self.collect_words('1990s', word)
        if year == '200':
            self.collect_words('2000s', word)
        if year == '201':
            self.collect_words('2010s', word)

    def most_common_words(self):
        filenames = glob.glob("../data/lyrics_tagged/*.txt")
        for filename in filenames:
            try:
                with codecs.open(filename, "r","utf8") as f:
                    lines = f.readlines()
                    for line in lines:
                        if "year" in line:
                            year = line[6:9]
                    for line in lines:
                        if "Lemma" in line:
                            word = self.clean_word(line[8:len(line)])
                            if re.search('[a-zA-Z]', word) == None:
                                self.add_words(year, word)
            except:
                continue

counting = Counting()
with codecs.open("words_appearence.json", "w", "utf8") as word_appearance:
    word_appearance.write(json.dumps(counting.word_appear, ensure_ascii=False))