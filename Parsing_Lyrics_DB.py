import xml.etree.ElementTree as ET
import glob
import codecs
import re


class Parsing:

    def __init__(self):
        self.all_words = set()

    def all_words_appear(self):
        filenames = glob.glob("../data/Lyrics/*/*.xml")
        for filename in filenames:
            try:
                with codecs.open(filename, "r", "utf8") as f:
                    tree = ET.parse(f)
                    root = tree.getroot()
                    lgs = root[1][0][0]
                    for lg in lgs:
                        for l in lg:
                            words = l.text.split(' ')
                            for word in words:
                                if not word in self.all_words:
                                    if re.search('[a-zA-Z]', word) == None: # we want only the Hebrew words
                                        self.all_words.add(word)
                                        with codecs.open("../data/words_to_tag.txt", "a", "utf8") as words_to_tag:
                                            words_to_tag.write(word + "\n")
            except:
                continue

parsing = Parsing()
parsing.all_words_appear()
