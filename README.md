# entro.py
entro.py is a module that calculates basic informational parameters for any input string. To use, simply download the file "entro.py" into
your working directory and load it like any other package. Make sure to define your input sequence as a string ```sequence = "etc"``` or load a plaintext file
```
import entro

sequence = "etc"

with open('etc.txt', 'r') as file:
    sequence = file.read().replace('\n', '')
```

The theory underpinning the program can be found in "THEORY.md." It describes how and why to calculate the parameters that
we can. Familiarity with Boltzmann entropy is recommended, but not required.

## $H_{1}^{Max}$ : State of Equiprobability
```
def max(sequence):
    return math.log2(len(set(Counter(sequence).elements())))
```
#### Description
```entro.max(sequence)``` calculates the maximum entropy of an alphabet. Time complexity of $O(1)$.

#### Arguments
**sequence** is a string variable.

## $f_i$ : Singlet Frequencies
```
def fi(sequence):
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))

    return fi
```
#### Description
```entro.fi(sequence)``` calculates $f_i$ for a target sequence. Time Complexity of $O(N)$.

#### Arguments
**sequence** is a string variable.

## $H_1$ : Shannon Entropy
```
def h(sequence):
    fi = []
    h1 = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))
    
    for x in fi:
        h1.append(x*math.log2(x))

    return -(sum(h1))
```
#### Description
```entro.h(sequence)``` calculates the $H_1$ of a target sequence. Also calculates: $f_i$. Time complexity of $O(N)$.

#### Arguments
**sequence** is a string variable.

## $D_1$ : Divergence from Equiprobability
```
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
```
#### Description
```entro.d1(sequence)``` calculates the $D_1$ of a target sequence. Also calculates: $H_{1}^{Max}$, $H_1$, and $f_i$. Time complexity of $O(N)$.

#### Arguments
**sequence** is a string variable.

## $f_{ij}$ : Doublet Frequencies
```
def fij(sequence):
    nn = []
    fij = []
    
    for (x, y), count in Counter(zip(sequence, sequence[1:])).items():
        nn.append(x + y)
        fij.append(count / (len(sequence)-1))
    
    return fij
```
#### Description
```entro.fij(sequence)``` returns a 1D array of $f_{ij}$. Time complexity of $O(N^2)$.

#### Arguments
**sequence** is a string variable.

## $D_2$ : Divergence from Independence
```
def h2i(sequence):
    
    # Singlet Frequencies
    fi = []
    for x in set(Counter(sequence).elements()):
        fi.append(Counter(sequence)[x] / len(sequence))
    
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
```
#### Description
```entro.h2i(sequence)``` returns the $D_2$ for a target sequence. Also calculates: $H_1$, $f_i$, $f_{ij}$, $H_{2}^{ind}$, and $H_2$.
Time complexity of $O(N^2)$.

#### Arguments
**sequence** is a string variable.

## $I_d$ : Information Density
```
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
```
#### Description
```entro.id(sequence)``` returns the $I_d$ of a target sequence. Also calculates: $H_{1}^{Max}$, $H_1$, $D_1$, $f_i$, $f_{ij}$,
and $H_{2}^{ind}$. Time complexity of $O(N^2)$.

#### Arguments
**sequence** is a string variable.

## $H_M$ : Markov Entropy
```
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
```
#### Description
``` entro.hm(sequence)``` returns the Markov entropy for a target string. Also calculates: $H_1$, $f_i$, $f_{ij}$, and $H_2$.
Time complexity of $O(N^2)$.

#### Arguments
**sequence** is a string variable.

## Technical Aside
**TL;DR**: The functions for calculating *doublet frequencies* and *divergence from independence* are both $O(N^2)$ with the
size of the alphabet. Unfortunately, this is unavoidable as it arises from the underlying math involved in calculating the
doublet frequencies. Please use caution for larger alphabets!

It is also recommended to assign the output of each function to a variable in order to save computation time, as each function calculates
all previous parameters necessary to calculate the value of interest.

#### Theoretical Basis
In the original literature (published 1972) Gatlin references the *nearest-neighbor* experiments and uses those results to
calculate the doublet frequencies. This will not be the method used here as it is a bit antiquated. It should be noted that
the first viable method of genome sequencing, Sanger sequencing, would not be invented until 1977. Yet still, viable full-genome
sequncing wouldn't become commonplace until the turn of the century, much less *affordable* genome sequencing ten years after.

The point of my program, *entro.py* is to bring her analysis into the 21st century by adapting the methods to work with full
genome sequences (which may be obtained independently or from the NIH repositries). Briefly, I will describe the method used
in this code to calculate the doublet frequencies.
R.A. Elton (1975) describes a method not based on the nearest-neighbor experiments:

>The sequence can be represented by $(x_{l}, ... , x_{n+1})$, using the convention that each value $x_i$ is 1, 2, 3 or 4
according as the ith base in the sequence is U(T), C, A or G. The transition count is then a 4x4 matrix of frequencies { $f_{ij}$ }, where $f_{ij}$ is the number of times that a base *i* in the sequence is followed by a base *j*.

Since we are using python, we do not need to use the cited convention that "each value $x_i$ is 1, 2, 3 or 4," but rather may
simply use the ```Counter()``` function to identify the number of times a doublet appears in a given sequence.

Just as one would find the frequency of a singlet by counting its occurence in a given sequence, then dividing it by the
total length of the sequence, we may find the doublet frequencies in a similar fashion. In order to determine the frequencies
of each doublet, the occurence must be divided by the "doublet space," i.e. the total amount of *possible* doublets. Consider
the following sequence ```genome = "AGCTTTTCA"```. It can be seen that ```len(genome) = 9``` but that the amount of doublets is 8.
This follows for even sequences too, ```genome = "AGCTTTTC"``` which has ```len(genome) = 8``` with a doublet space of 7. So it
can be seen that the doublet space is always $n-1$ or ```len(genome)-1```. This can be proved more rigorously by noting that each
single base in the sequence may serve as the "root" of a doublet pair. Moving left to right through the sequence, no matter the
length, there will always be a doublet pair that is comprised of the last base and a "null" value outside the sequence, so to speak.
The base at the end of the sequence will always be left out. This is accounted for by $n-1$.

Therefore, we may construct the sample space for doublets, $S_2$, from the sample space of singlets, $S_1$, as follows:
```
n = ["A", "T", "C", "G"]
nn = []
fij = []

for x in n:
  for y in n:
    nn.append(x + y)
    fij.append(genome.count(x + y) / (len(genome)-1))
```
where $S_1$ is represented by ```n = ["A", "T", "C", "G"]```. $S_2$ is constructed by looping through $S_1$ twice and appending
the doublets into a new list, ```nn = []```. At the same time, the frequencies, $f_{ij}$ are calculated by counting the occurence
of a given doublet, ```for (x, y), count in Counter(zip(sequence, sequence[1:])).items()``` and dividing it by the aforementioned doublet space, ```len(genome)-1```. This is
all appended to a list of doublet frequencies, ```fij = []```. The nested for loops in effect are the same method described by
R.A. Elton, but instead of keeping it in a 4x4 matrix, the results are appended into a 1-dimensional list.

As such, *is important to note* that the time complexity of these two particular functions (doublet frequencies & divergence from
independence) are $O(N^2)$ with the size of the input alphabet (the ```.Counter()``` function is $O(N)$ ). While this is trivial for small
alphabets (like that of the genome) it will become computationally prohibitive at larger input spaces.

Furthermore, each function calculates all values *from scratch.* To take one of the largest functions as an example, in order to calculate
$I_d$, we must also calculate $H_{1}^{Max}$, $H_1$, $D_1$, $f_i$, $f_{ij}$, $H_{2}^{ind}$, and $D_2$. Most of which are $O(N^2)$ to the
alphabet. In light of this, it is **highly** recommended that when using these function to assign their output to a variable so that you
are not calculating the value from scratch each time.
