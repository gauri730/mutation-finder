def parse_fasta(filepath):
    seq= []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith ('>'):
                continue
            elif line:
                seq.append(line)
    res = ''.join(seq).upper()
    val_bases= set('ACGTN')
    invalid_chars = set(res) - val_bases
    if invalid_chars:
         print(f"Unexpected characters to be found: {invalid_chars}")
    return res
