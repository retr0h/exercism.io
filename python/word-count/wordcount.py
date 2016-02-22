from collections import defaultdict


def word_count(phrase):
    seen = defaultdict(int)
    decoded_phrase = phrase.decode('utf-8')
    sanitized_phrase = ''.join(c if c.isalnum() else ' '
                               for c in decoded_phrase)
    for word in sanitized_phrase.split():
        seen[word.lower()] += 1

    return seen
