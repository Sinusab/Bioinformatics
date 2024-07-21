# Sinus_alpha

def Reverse_complement(DNA):
    DNA = DNA.upper()
    complementary = ''
    for i in range(len(DNA),0,-1):
        if DNA[i-1] == 'A':
            complementary += 'T'
        if DNA[i-1] == 'T':
            complementary += 'A'
        if DNA[i-1] == 'C':
            complementary += 'G'
        if DNA[i-1] == 'G':
            complementary += 'C'
    return complementary

# Testing
DNA = (
    "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtgga"
    "tgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagag"
    "aggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgcc"
    "atattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatct"
    "tgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctg"
    "acatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccga"
    "ttgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttcc"
    "ttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"
)

print(Reverse_complement(DNA))