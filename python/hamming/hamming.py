def distance(strand1, strand2):
    hamming_distance = 0
    strand2_list = list(strand2)
    for i, n in enumerate(strand1):
        if n != strand2_list[i]:
            hamming_distance += 1
    return hamming_distance
