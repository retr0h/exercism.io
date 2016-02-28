import string


def is_pangram(phrase):
    """ Pangrams are words or sentences containing every letter
    of the alphabet at least once; the best known English example
    being A quick brown fox jumps over the lazy dog.
    """
    seen = dict.fromkeys(string.ascii_lowercase, 0)
    for c in phrase:
        seen[c.lower()] = 1

    if 0 in seen.values():
        return False
    return True
