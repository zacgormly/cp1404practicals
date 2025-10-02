"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
WILDCARDS = "%#*"
ALPHABET = string.ascii_lowercase


combined_choices = WILDCARDS + ALPHABET
word_length = int(input("Word length: "))

word = ""
for i in range (word_length):
    word_format = random.choice(combined_choices)
    for kind in word_format:
        if kind == "%":
            word += random.choice(CONSONANTS)
        elif kind == "#":
            word += random.choice(VOWELS)
        elif kind == "*":
            word += random.choice(string.ascii_lowercase)
        else:
            word += kind

print(word)