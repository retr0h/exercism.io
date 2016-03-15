import string


def decode(cipher):
    cipher = ''.join(cipher.split())
    cipher = cipher.lower()
    translation_table = string.maketrans(string.ascii_lowercase[::-1],
                                         string.ascii_lowercase)

    return cipher.translate(translation_table)


def encode(plain):
    plain = plain.lower()
    plain = ''.join(plain.split())
    plain = ''.join(c for c in plain if c not in string.punctuation)
    plain = ' '.join([plain[i:i + 5] for i in range(0, len(plain), 5)])
    translation_table = string.maketrans(string.ascii_lowercase,
                                         string.ascii_lowercase[::-1])

    return plain.translate(translation_table)
