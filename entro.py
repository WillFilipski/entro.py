import math

genome = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGCTTCTGAACCTG"
n = ["A", "T", "C", "G"]

#STATE OF EQUIPROBABILITY
H1max = math.log2(len(n))

#SINGLET FREQUENCIES
fi = []

for x in n:
    fi.append(genome.count(x) / len(genome))
    print(f'p({x}) = {genome.count(x) / len(genome)}')

#SHANNON ENTROPY
h1 = []
for x in fi:
    h1.append(x*math.log2(x))

H1 = -(sum(h1))
print(f'Shannon Entropy, H1 = {H1} bits')

#DIVERGENCE FROM EQUIPROBABILITY
D1 = H1max - H1
print(f'Divergence from equiprobability, D1 = {D1} bits')

#DOUBLET FREQUENCIES
nn = []
fij = []

for x in n:
  for y in n:
    nn.append(x + y)
    
    fij.append(genome.count(x + y) / (len(genome)-1))
    print(f'p({x}{y}) = {genome.count(x + y) / (len(genome)-1)}')

#DIVERGENCE FROM INDEPENDENCE
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
print(f'Divergence from independence, D2 = {D2} bits')

#INFORMATION DENSITY
Id = D1 + D2
print(f'Information Density, Id = {Id} bits')

#MARKOV ENTROPY
Hm = H2 - H1
print(f'Markov entropy, Hm = {Hm} bits')