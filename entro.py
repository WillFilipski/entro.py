import math

#STATE OF EQUIPROBABILITY
def max(n):
    return math.log2(len(n))

#SINGLET FREQUENCIES
def fi(n, sequence):
    fi = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))
        
    return fi

#SHANNON ENTROPY
def h(n, sequence):
    fi = []
    h1 = []
    for x in n:
        fi.append(sequence.count(x) / len(sequence))
    
    for x in fi:
        h1.append(x*math.log2(x))

    return -(sum(h1))

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

#DOUBLET FREQUENCIES
def fij(n, sequence):
    nn = []
    fij = []

    for x in n:
        for y in n:
            nn.append(x + y)
    
            fij.append(sequence.count(x + y) / (len(sequence)-1))
    
    return fij

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

#MARKOV ENTROPY
def hm(n, sequence):
    # Singlet Frequencies
    fi = []

    for x in n:
        fi.append(sequence.count(x) / len(sequence))

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
            fij.append(sequence.count(x + y) / (len(sequence)-1))

    # Doublet Entropy
    h2 = []
    for x in fij:
        h2.append(x*math.log2(x))

    H2 = -(sum(h2))

    return H2 - H1
