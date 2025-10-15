"""
Word Occurrences
Estimate: 25 minutes
Actual:   28 minutes
"""


def main():
    """Determine count of each word in a string of text."""
    text = input("Text: ")
    words = text.split()
    word_to_count = count_words(words)

    maximum_word_length = max((len(word) for word in words))

    for word, count in sorted(word_to_count.items()):
        print(f"{word:{maximum_word_length}} : {count}")


def count_words(words):
    """Count instances of each word and store in dictionary."""
    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1
    return word_to_count


main()
