# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
#
# Example: (input --> output)
#
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
# dnaStrand []        `shouldBe` []
# dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
# dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
# dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]

dna_pairs = {'A':'T',
             'C':'G',
             'T':'A',
             'G':'C'}

list_converted = []

def DNA_strand(dna):
    list_converted = []
    for letter in dna:
        converted = dna_pairs.setdefault(letter)
        list_converted.append(converted)
        outcome = ''.join(list_converted)
    return outcome


dna = 'AAAA'
print(DNA_strand(dna))

dna = 'TTTT'
print(DNA_strand(dna))


# Other try
# strand_sep = list(dna_strand)
# print(strand_sep)

# for letter in strand_sep:
#     if letter == 'A':
#         letter = 'T'
#         print(letter)

# new_strand = ''.join(strand_sep)
# print(new_strand)