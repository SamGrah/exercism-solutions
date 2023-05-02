STOP_CONDONS = ['UAA', 'UAG', 'UGA']

CONDON_PROTIEN_MAP = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCA': 'Serine',
    'UCC': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan'
}


def proteins(strand):
    idx = 3
    proteins_list = []
    while idx <= len(strand):
        condon = ''.join(strand[idx - 3:idx])
        if condon in STOP_CONDONS:
            break
        protein = CONDON_PROTIEN_MAP[condon]
        proteins_list.append(protein) 
        idx += 3
    return proteins_list
