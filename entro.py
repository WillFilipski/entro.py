import math
from collections import Counter


#STATE OF EQUIPROBABILITY
def max(sequence):
    return math.log2(len(set(Counter(sequence).elements())))

#SINGLET FREQUENCIES
def fi(sequence):
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))

    return fi

#SHANNON ENTROPY
def h(sequence):
    fi = []
    h1 = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))
    
    for x in fi:
        h1.append(x*math.log2(x))

    return -(sum(h1))

#DIVERGENCE FROM EQUIPROBABILITY
def d1(sequence):

    # Singlet Frequencies
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))
    
    #Shannon Entropy
    h1 = []
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))
    H1max = math.log2(len(n))
    return H1max - H1

#DOUBLET FREQUENCIES
def fij(sequence):
    nn = []
    fij = []
    
    for (x, y), count in Counter(zip(sequence, sequence[1:])).items():
        nn.append(x + y)
        fij.append(count / (len(sequence)-1))
    
    return fij

#DIVERGENCE FROM INDEPENDENCE
def h2i(sequence):
    
    # Singlet Frequencies
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))
    
    # Shannon Entropy
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))
    
    # Doublet Frequencies
    nn = []
    fij = []
    
    for (x, y), count in Counter(zip(sequence, sequence[1:])).items():
        nn.append(x + y)
        fij.append(count / (len(sequence)-1))
    
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
def id(sequence):

    # State of Equiprobaility
    H1max = math.log2(len(set(Counter(sequence).elements())))

    # Singlet Frequencies
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))

    # Shannon Entropy
    h1 = []
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))

    # Divergence from Equiprobability
    D1 = H1max - H1
    
    # Doublet Frequencies
    nn = []
    fij = []
    
    for (x, y), count in Counter(zip(sequence, sequence[1:])).items():
        nn.append(x + y)
        fij.append(count / (len(sequence)-1))
    
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
def hm(sequence):
    # Singlet Frequencies
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))

    # Shannon Entropy
    h1 = []
    for x in fi:
        h1.append(x*math.log2(x))

    H1 = -(sum(h1))

    # Doublet Frequencies
    nn = []
    fij = []
    for (x, y), count in Counter(zip(sequence, sequence[1:])).items():
        nn.append(x + y)
        fij.append(count / (len(sequence)-1))

    # Doublet Entropy
    h2 = []
    for x in fij:
        h2.append(x*math.log2(x))

    H2 = -(sum(h2))

    return H2 - H1
