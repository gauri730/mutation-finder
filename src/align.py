def build_matrix(ref, sample, match_score=1, mismatch_pen=-1, gap_pen=-2):
    m = len(ref)
    n = len(sample)
    matrix = [[0 for _ in range(n + 1)] for _  in range(m + 1)]
    for k  in range(m + 1):
        matrix[k][0] = k * gap_pen
    for l  in range(n + 1):
        matrix[0][l] = l * gap_pen
    return matrix
if __name__ == "__main__":
    test_matrix = build_matrix("GAT", "GCT")
    for row in test_matrix:
        print(row)
