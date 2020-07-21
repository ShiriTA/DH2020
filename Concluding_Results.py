import codecs
import json

with codecs.open("../data/words_appearence.json", "r", "utf8") as word_appearance:
    word_appear = json.load(word_appearance)
    new_dict = {'1970s': dict(), '1980s': dict(), '1990s': dict(), '2000s': dict(), '2010s': dict()}
    for key in word_appear.keys():
        dct = word_appear[key]
        for dc_key in dct.keys():
            val = dct[dc_key]
            if val > 40:
                new_dict[key][dc_key] = val


with codecs.open("../data/words_appearence_com.json", "a", "utf8") as common:
    common.write(json.dumps(new_dict, ensure_ascii=False))