"""
Word Occurrences
Estimate: 25 minutes
Actual:   24 minutes
"""


def main():
    word_to_count = {}
    text = input("Text: ")
    words = text.split()
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    maximum_word_length = max((len(word) for word in words))

    for word, count in sorted(word_to_count.items()):
        print(f"{word:{maximum_word_length}} : {count}")


main()
