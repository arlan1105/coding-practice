def DNA_strand(dna):
    opp = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    return dna.translate(str.maketrans(opp))

print(DNA_strand('ATCG'))

# import string
# def DNA_strand(dna):
#     return dna.translate(string.maketrans("ATCG","TAGC"))