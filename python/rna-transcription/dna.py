map = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}


def to_rna(dna_strand):
    rna_list = [map.get(s) for s in list(dna_strand)]
    return ''.join(rna_list)