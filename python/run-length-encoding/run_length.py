import itertools
import re


def encode(data):
    pairs = []
    for name, group in itertools.groupby(data):
        group_size = len(list(group))
        if group_size > 1:
            pairs.append(u'{}{}'.format(group_size, name))
        else:
            pairs.append(u'{}'.format(name))

    return ''.join(pairs)


def decode(data):
    return re.sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)), data)
