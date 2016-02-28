TRANSLATIONS = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    rna_list = [TRANSLATIONS.get(s) for s in dna_strand]

    return ''.join(rna_list)
