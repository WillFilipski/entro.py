# entro.py
entro.py calculates basic informational parameters for any input string. To use, simply download the file "entro.py" into
your working directory and load it like any other package.

The theory underpinning the program can be found in "THEORY.md." It describes how and why to calculate the parameters that
we can. Familiarity with Thermodynamic Entropy is recommended, but not required.

## The Modules

(WIP)

## Time Complexity
*TL;DR*: The functions for calculating *doublet frequencies* and *divergence from independence* are both $O(N^2)$ with the
size of the alphabet. Unfortunately, this is unavoidable as it arises from the underlying math involved in calculating the
doublet frequencies. Please use caution for larger alphabets!

#### Technical Aside
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

By the grace of python, we do not need to use the cited convention that "each value $x_i$ is 1, 2, 3 or 4," but rather may
simply use the ```count()``` function to identify the number of times a doublet appears in a given sequence.

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
of a given doublet, ```genome.count(x + y)``` and dividing it by the aforementioned doublet space, ```len(genome)-1```. This is
all appended to a list of doublet frequencies, ```fij = []```. The nested for loops in effect are the same method described by
R.A. Elton, but instead of keeping it in a 4x4 matrix, the results are appended into a 1-dimensional list.

As such, *is important to note* that the time complexity of these two particular functions (doublet frequencies & divergence from
independence) are $O(N^2)$ with the size of the input alphabet (the ```.count()``` function is $O(N)$ ). While this is trivial for small
alphabets (like that of the genome) it will become computationally prohibitive at larger input spaces.
