def distance(strand_a, strand_b):
    length_strand_a = len(strand_a)
    length_strand_b = len(strand_b)
    is_unequal_lengths = length_strand_a != length_strand_b
    if is_unequal_lengths:
        raise ValueError('Strands must be of equal length.')

    hamming_distance = 0
    for idx in range(0, length_strand_a):
        if strand_a[idx] != strand_b[idx]:
            hamming_distance += 1
    return hamming_distance
