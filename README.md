# entro.py

###Introduction

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

##Shannon Entropy
Statistical thermodynamics, which we have been discussing, is based on the assumption that all microstates are equiprobable.
If this is the case, then the probability of each individual microstate, $p_{i}$, is simply one out of the total number of
microstates, *W*, i.e.,
$p_{i}= \frac{1}{W}$ or $W= \frac{1}{p_{i}}$
Substituting this expression of *W* in equation (3) yields,
$$S=K \log \frac{1}{p_{i}}$$
which furthur simplifies to equation (9):
$$S=-K \log p_{i}$$
Keep in mind that equation (9) only holds for the case in which the microstates are equiprobable. Developing the idea further,
the expectation value of a numerical-valued random phenomenon is the sum over all possible outcomes of the probability of each
individual outcome multiplied by the numerical value of that individual outcome:
$$E_{x}=\sum_{i} p_{i} n_{i}$$
With every arrangement of the system there is associated the number $-K log p_{i}$, and the probability of each arrangement $p_{i}$.
The expectation value of this numerical-valued random phenomenon, which we will denote *H*, is
$$H=-K \sum_{i} p_{i} \log p_{i}$$
This is Shannon's formula. It is the expectation value of the Boltzmann variable, $-K log p_{i}$. It expresses the entropy of
a system in terms of probabilities and may be used even when all the microstates or elementary arrangements of the system are
not equiprobable.
As for units, the logarithm base we use is of arbitrary choice, and the value of the proportionality constant is also arbitrary.
When *K* is set to equal to 1 and base 2 logarithms are used, the unit of entropy is called a bit.

###Divergence from Equiprobability
The power of Shannon's formula lies in its generality. The $p_{i}$ may refer to the probabilites of *any* elementary events
defined on *any* sample description space. We may apply this concept to the description space of DNA: $S_{1} = {A, T, C, G}$
The entropy of this space is known:
$$H_{1} = -K \sum_{i} p_{i} \log p_{i}$$
But the $p_{i}$ are known, they are simply the composition of the DNA molecule. Let us consider the scenario where all bases
are equiprobable, $p(A) = p(T) = p(C) = p(g) = \frac{1}{4}$:
$$H_{1} = - \log \frac{1}{4} = \log 4$$
$$H_{1} = 2 \bits$$
