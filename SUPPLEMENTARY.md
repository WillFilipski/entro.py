# entro.py
The following is a paraphrased introduction to several concepts from information theory taken from the text
*Information Theory & the Living System* by Lila L. Gatlin. It describes how and why we are calculating the
quantities that we are, and why they are significant. Although the theory can be applied to any string
consisting of any number of letters, the example and applications here will be for DNA.

## Introduction

Entropy measures the degree of randomness of a system. It is inversely proportional to the information of the system,
such that the maximum entropy state is characterized by equiprobable, independent elementary events. The intuitive
idea is that the most random state is characterized by equiprobable events. For example a "fair" die is one this is
perfectly balanced so that all sides have an equally probable chance of appearing on a given roll. 

In thermodynamics, physicists call a spcific arrangement of a system a "microstate." The exact number of microstates
possible for a given macrostate is the "thermodynamic probability" of that macrostate and is denoted by the letter *W*.
As the number of microstates increases, the entropy increases. We might at first attempt to express this relationship
as a direct proportion. Hence for a given macrostate we might write: $S=KW$ (1), where *S* denotes the entropy, *W* is the
thermodynamic probability, and *K* is an arbitrary constant. However, the definition is not yet complete or even correct.

It is intuitively reasonable that entropy should also have an additive property, i.e. the entropy of system *A* plus the
entropy of system *B* should be equal to the entropy of the composite system *AB*: $S_{A}+S_{B} = S_{AB}$ (2). Boltzmann solved
this problem in the early 19th century. When numbers are expressed as powers of the same base are multiplicative, their
exponents are additive. Logarithms are such exponents. Therefore we can combine both properties (1) & (2) in equation (3):
$$S=K \log W$$
Thus the entropy of system *A* may be written
$$S_{A}=K \log W_{A}$$
and system *B*
$$S_{B}=K \log W_{B}$$
Adding these entropies, we have the entropy of the composite system,
$$S_AB=K \log W_{A}+KlogW_{B}$$
Such that
$$S_{AB}=K \log W_{A}W_{B}$$
or
$$S_{AB}=K \log W_{AB}$$
It can be seen that Boltzmann's definition has both desired properties.

## Shannon Entropy
Statistical thermodynamics, which we have been discussing, is based on the assumption that all microstates are equiprobable.
If this is the case, then the probability of each individual microstate, $p_{i}$, is simply one out of the total number of
microstates, *W*, i.e.,
$p_{i}= \frac{1}{W}$ or $W= \frac{1}{p_{i}}$
Substituting this expression of *W* in equation (3) yields,
$$S=K \log \frac{1}{p_{i}}$$
which furthur simplifies to equation (4):
$$S=-K \log p_{i}$$
Keep in mind that equation (4) only holds for the case in which the microstates are equiprobable. Developing the idea further,
the expectation value of a numerical-valued random phenomenon is the sum over all possible outcomes of the probability of each
individual outcome multiplied by the numerical value of that individual outcome:
$$E_{x}=\sum_{i} p_{i} n_{i}$$
With every arrangement of the system there is associated the number $-K \log p_{i}$, and the probability of each arrangement $p_{i}$.
The expectation value of this numerical-valued random phenomenon, which we will denote *H*, is
$$H=-K \sum_{i} p_{i} \log p_{i}$$
This is Shannon's formula. It is the expectation value of the Boltzmann variable, $-K \log p_{i}$. It expresses the entropy of
a system in terms of probabilities and may be used even when all the microstates or elementary arrangements of the system are
not equiprobable.
As for units, the logarithm base we use is of arbitrary choice, and the value of the proportionality constant is also arbitrary.
When *K* is set to equal to 1 and base 2 logarithms are used, the unit of entropy is called a bit.

## Divergence from Equiprobability
The power of Shannon's formula lies in its generality. The $p_{i}$ may refer to the probabilites of *any* elementary events
defined on *any* sample description space. We may apply this concept to the description space of DNA: $S_{1} = {A, T, C, G}$
The entropy of this space is known:
$$H_{1} = -K \sum_{i} p_{i} \log p_{i}$$
But the $p_{i}$ are known, they are simply the composition of the DNA molecule. Let us consider the scenario where all bases
are equiprobable, $p(A) = p(T) = p(C) = p(G) = \frac{1}{4}$:
$$H_{1} = - \log \frac{1}{4} = \log 4$$
$$H_{1} = 2 \text{ bits} $$
Since all the bases are equiprobable, this is the maximum value that $H_{1}$ can ever have. More generally, let *a* be the number
of letters/symbols in an alphabet/sequence (*a* is 4 for DNA), therefore:
$$p_{i} = \frac{1}{a}$$
and
$$H_{1} = -\log p_{i} = -\log \frac{1}{a} = \log a$$
The divergence from this equiprobable state, which we may call $D_{1}$, is the maximum value $H_{1}$ can have, minus the value it
actually does have.
$$D_{1} = H_{1}^{Max} - H_{1} = \log a - H_{1}$$

## Divergence from Independence
It is easy to see that $D_{1}$ and $H_1$ tell us only part of the story. They are both based on $S_1$, a space of single-letter
events, which contains no information on how these letters are arranged in a linear sequence. $H_1$ is only a function of the
base composition of the sequence. We said that the maximum entropy state is characterized by equiprobable and independent events.
Therefore we must ask the question "Does the occurence of any one base along the chain alter the probability of occurence of the
base next to it?" This is not an entirely pointless inquiry, as stated by R.A. Elton (1975):

>What determines the order of bases in a particular nucleic acid sequence? The widely accepted answer is that ancestral sequences have been moulded
by mutation and subsequent selection to give rise to the surviving descendants we see today. The relevance of this basic concept to the statistical analysis of sequences is that we can consider the ordering of bases to be under the influence of two factors, random and systematic. These would essentially correspond to the mutation and selection aspects of evolution, in that two sequences under the same selective pressure would be expected to show the same general trends in the frequency of given sub-sequences, but would differ randomly from one another as a result of different chance occurrences of mutational change.

If we could measure these conditional probablities in some way, and if we were to find that they were the same as the base composition, i.e.,
$$p(A|A) = p(A)$$
$$p(T|A) = p(T)$$
$$p(C|A) = p(C)$$
$$p(G|A) = p(G)$$
then the bases would be independent of each other. However, if we were to find that the conditional probabilities were *not* the
same as the base composition, then there would be some divergence from the independence of the bases. We can define the sample
description space for doublet (letter pair) sequences as:
$$S_{2} = \lbrace AA, AT, AC, AG, TA, TT, TC, TG, CA, CT, CC, CG, GA, GT, GC, GG \rbrace $$
And therefore the entropy, $H_{2}$, of the description space $S_{2}$ represented by equation (5):
$$H_{2} = -[p(AA) \log p(AA) + p(AT) \log p(AT) + ...]$$
But what is the probability of the doublet event? This is described in more detail below, in the *technical aside*.
The takeaway is that DNA bases *are not* independent events, nor should we have expected them to be. Solving equation (5) will
give the value of $H_2$ when the bases are *dependent*, which we may denote as $H_2^D$. We may also solve equation (5) for the
scenario in which the bases are *independent*, i.e. $p(AA) = p(A) \times p(A)$. We will call this entropy $H_2^{Ind}$.

Finally, the **divergence from independence**, which we will call $D_2$, is simply the difference between the two.
$$D_2 = H_2^{Ind} - H_2^D$$
The sum of $D_1$ and $D_2$ is the total divergence from the maximum entropy state $\log a$.

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

## Potential versus Stored Information
Potential information is vital to communication. Without the element of of potential variety and uncertainty about what will come
next, there can be no transmission of information. In fact, the entropy of Shannon's formula is usually referred to as "information"
throughout the literature and sometimes as "information content." Are we to conclude then that as the entropy increases the
information always increases? No, it is not quite this simple. Stored information is associated with the ordering process brought
about by the constraints of a language or any organized information storage process. Since stored information varies inversely with
entropy, lowered entropy means a higher capacity to store information. This is precisely what we have been calculating in $D_1$ and $D_2$,
whose sum measures exactly how much the entropy has been lowered from the maximum entropy state. Thus we may define stored information, $I_s$, as
$$I_s = D_1 + D_2$$
