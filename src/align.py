from parser import parse_fasta
def build_matrix(ref, sample, match_score=1, mismatch_pen=-1, gap_pen=-2):
    m  = len(ref)
    n  = len(sample)
    matrix = [[0 for _ in range(n + 1)] for _  in range(m + 1)]
    for k  in range(m + 1):
        matrix[k][0] = k * gap_pen
    for l  in range(n + 1):
        matrix[0][l] = l * gap_pen
    for k in range (1, m+1):
        for l in range( 1, n+1):
            if ref[k - 1] == sample[l - 1]:
                diag = matrix[k - 1][l- 1] + match_score
            else:
                diag = matrix[k - 1][l - 1] + mismatch_pen
            up = matrix[k - 1][l] + gap_pen
            left = matrix[k][l - 1] + gap_pen
            matrix[k][l] = max(diag, up, left)
    return matrix
def traceback(matrix, ref, sample, match_score=1, mismatch_pen=-1, gap_pen=-2):
    k= len(ref)
    l = len(sample)
    aligned_ref = []
    aligned_sample = []
    while k > 0 and l >0:
        curr = matrix[k][l]
        if ref[k - 1] == sample[l - 1]:
            diag_score = matrix[k - 1][l - 1] + match_score
        else:
            diag_score = matrix[k - 1][l - 1] + mismatch_pen
        if curr == diag_score:
            aligned_ref.append(ref[k - 1])
            aligned_sample.append(sample[l - 1])
            k = k - 1
            l = l - 1
        elif curr == matrix[k - 1][l] + gap_pen:
            aligned_ref.append(ref[k - 1])
            aligned_sample.append('-')
            k = k - 1
        else:
            aligned_ref.append('-')
            aligned_sample.append(sample[l - 1])
            l = l - 1
    while k  > 0:
        aligned_ref.append(ref[k - 1])
        aligned_sample.append('-')
        k = k - 1
    while l  > 0:
        aligned_ref.append('-')
        aligned_sample.append(sample[l - 1])
        l = l - 1
    aligned_ref.reverse()
    aligned_sample.reverse()
    return ''.join(aligned_ref), ''.join(aligned_sample)

def classify_variants(aligned_ref, aligned_sample):
    variants = []
    for pos in range(len(aligned_ref)):
        ref_char = aligned_ref[pos]
        sample_char = aligned_sample[pos]
        if ref_char == sample_char:
            continue
        elif ref_char == '-':
            variants.append((pos, 'Insertion', ref_char, sample_char))
        elif sample_char == '-':
            variants.append((pos, 'Deletion', ref_char, sample_char))
        else:
            variants.append((pos, 'SNP', ref_char, sample_char))
    return variants


if __name__ == "__main__":
    ref = parse_fasta('data/reference.fasta')
    sample = parse_fasta('data/sample.fasta')
    test_matrix = build_matrix(ref, sample)
    for row in test_matrix:
        print(row)
    aligned_ref, aligned_sample = traceback(test_matrix, ref, sample)
    print("Aligned ref:   ", aligned_ref)
    print("Aligned sample:", aligned_sample)
    variants = classify_variants(aligned_ref, aligned_sample)
    print("Variants found:", variants)
