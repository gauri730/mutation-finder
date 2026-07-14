def build_matrix(ref, sample, match_score=1, mismatch_pen=-1, gap_pen=-2):
    m = len(ref)
    n = len(sample)
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
if __name__ == "__main__":
    test_matrix = build_matrix("GAT", "GCT")
    for row in test_matrix:
        print(row)
