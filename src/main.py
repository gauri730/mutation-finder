from parser import parse_fasta

ref = parse_fasta('data/reference.fasta')
samp = parse_fasta('data/sample.fasta')

print("Reference:", ref)
print("Sample:   ", samp)
print("Reference length:", len(ref))
print("Sample length:   ", len(samp))
