import phonetics as ph
import fuzzy
import requests
import jellyfish


# print(ph.dmetaphone("door"))

soundex = fuzzy.Soundex(4)

# x = soundex('fuzzy')
# print(x)

# dmeta = fuzzy.DMetaphone()
# print(dmeta('xsaiwwwdmo'))

print(jellyfish.metaphone('Antidisestablishmentarianism'))
print(jellyfish.soundex('Anathema'))

print(jellyfish.levenshtein_distance('response','answer'))