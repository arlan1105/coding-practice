def complementary_dna(strand):
    complement = {
    'A':'T', 
    'C':'G', 
    'T':'A', 
    'G':'C'
    }

    return strand.translate(str.maketrans(complement))

print(complementary_dna("ACGT"))

# return strand.translate(str.maketrans('ACGT', 'TGCA'))