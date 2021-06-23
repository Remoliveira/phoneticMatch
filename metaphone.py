import phonetics as ph
import fuzzy
from bs4 import BeautifulSoup
import jellyfish
import requests

url = "https://www.thoughtco.com/hard-to-pronounce-words-4156950"

page = requests.get(url)

pageSoup = BeautifulSoup(page.content, 'html.parser')

hardWords =  pageSoup.find_all('span',class_="mntl-sc-block-heading__text")

unWords = []
for words in hardWords:
    # print(words.text)
    unWords.append(words.text)

unWords.pop()

print(unWords)


# print(ph.dmetaphone("door"))

soundex = fuzzy.Soundex(4)

# x = soundex('fuzzy')
# print(x)

# dmeta = fuzzy.DMetaphone()
# print(dmeta('xsaiwwwdmo'))

# print(jellyfish.metaphone('Antidisestablishmentarianism'))
# print(jellyfish.soundex('Anathema'))

# print(jellyfish.levenshtein_distance('response','answer'))

