def sort(word):
    word = word.lower()
    return ''.join(sorted(word))


def is_anagram(word, possible_anagrams):
    for candidate in possible_anagrams:
        if sort(word) == sort(candidate) and word.lower() != candidate.lower():
            yield candidate


def detect_anagrams(word, possible_anagrams):
    return [candidate for candidate in is_anagram(word, possible_anagrams)]
