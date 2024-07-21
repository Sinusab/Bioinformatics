# Sinus_alpha

def pattern_count(text,pattern):
    count = 0
    for i in range(0,len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def frequent_words(text,k):
    frequent_patterns = set()
    counts = [0] * (len(text)-k + 1)

    for i in range (0,len(text)-k + 1):
        pattern = text[i:i+k]
        counts[i] = pattern_count(text,pattern)
    
    max_count = max(counts)

    for i in range(0,(len(text)- k + 1)):
        if counts[i] == max_count:
            frequent_patterns.add(text[i:i+k])

    return frequent_patterns

# print(pattern_count('ACAACTATGCATACTATCGGGAACTATCCT','ACTAT'))
# print(frequent_words('ACTGACTCCCACCCC',3))

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

# print(frequent_words(DNA,9))