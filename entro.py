import math

sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACCTG"
n = ["A", "T", "C", "G"]

#STATE OF EQUIPROBABILITY
def max(n):
    return math.log2(len(n))

# H1max = math.log2(len(n))

#SINGLET FREQUENCIES
def fi(n, sequence):
    fi = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))

print(f'p({x}) = {sequence.count(x) / len(sequence)}')

#SHANNON ENTROPY
def h(n, sequence):
    fi = []
    h1 = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))
    
    for x in fi:
        h1.append(x*math.log2(x))

    return -(sum(h1))

# print(f'Shannon Entropy, H1 = {H1} bits')

#DIVERGENCE FROM EQUIPROBABILITY
def d1(n, sequence):
    
    #Shannon Entropy
    fi = []
    h1 = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))
    
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))
    H1max = math.log2(len(n))
    return H1max - H1

# print(f'Divergence from equiprobability, D1 = {D1} bits')

#DOUBLET FREQUENCIES
def fij(n, sequence):
    nn = []
    fij = []

    for x in n:
        for y in n:
            nn.append(x + y)
    
            fij.append(sequence.count(x + y) / (len(sequence)-1))
    
    return fij

# print(f'p({x}{y}) = {sequence.count(x + y) / (len(sequence)-1)}')

#DIVERGENCE FROM INDEPENDENCE
def h2i(n, sequence):
    
    # Singlet Frequencies
    fi = []
    h1 = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))
    
    # Shannon Entropy
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))
    
    # Doublet Frequencies
    nn = []
    fij = []
    for x in n:
        for y in n:
            nn.append(x + y)
    
            fij.append(sequence.count(x + y) / (len(sequence)-1))
    
    #Divergence from Independence
    h2ind = []
    for x in fi:
        for y in fi:
            h2ind.append((x*y)*math.log2(x*y))

    H2ind = -(sum(h2ind))

    h2 = []
    for x in fij:
        h2.append(x*math.log2(x))

    H2 = -(sum(h2))
    
    return H2ind - H2

# print(f'Divergence from independence, D2 = {D2} bits')

#INFORMATION DENSITY
def id(n, sequence):

    # State of Equiprobaility
    H1max = math.log2(len(n))

    # Shannon Entropy
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))

    # Divergence from Equiprobability
    D1 = H1max - H1

    # Singlet Frequencies
    fi = []
    h1 = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))
    
    # Doublet Frequencies
    nn = []
    fij = []
    for x in n:
        for y in n:
            nn.append(x + y)
            fij.append(sequence.count(x + y) / (len(sequence)-1))
    
    # Divergence from Independence
    h2ind = []
    for x in fi:
        for y in fi:
            h2ind.append((x*y)*math.log2(x*y))

    H2ind = -(sum(h2ind))

    h2 = []
    for x in fij:
        h2.append(x*math.log2(x))

    H2 = -(sum(h2))
    D2 = H2ind - H2

    return D1 + D2

# print(f'Information Density, Id = {Id} bits')

#MARKOV ENTROPY
def hm(n, sequence):
    # Singlet Frequencies
    fi = []

    for x in n:
        fi.append(genome.count(x) / len(genome))

    # Shannon Entropy
    h1 = []
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))

    # Doublet Frequencies
    nn = []
    fij = []

    for x in n:
        for y in n:
            nn.append(x + y)
            fij.append(genome.count(x + y) / (len(genome)-1))

    # Doublet Entropy
    h2 = []
    for x in fij:
        h2.append(x*math.log2(x))

    H2 = -(sum(h2))

    return H2 - H1

# print(f'Markov entropy, Hm = {Hm} bits')