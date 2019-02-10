def to_rna(dna_strand):
    _dna = "GCTA"
    _rna = "CGAU"
    rna_strand = ""

    for l in dna_strand:
        for dna, rna in zip(_dna, _rna):
            if l == dna:
                rna_strand += rna
                
    return rna_strand