# Longest Common Subsequence of Two Sequences

Compute the longest common subsequence of 
two integer sequences of length at most 100.

Given two sequences 
A = (a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>) and 
B=(b<sub>1</sub>, b<sub>2</sub>, ..., b<sub>m</sub>), find the 
length of their longest common subsequence, 
i.e., the largest non-negative integer p such that 
there exist indices
1 &leq; i<sub>1</sub> < i<sub>2</sub> <  &ctdot; <  i<sub>p</sub> &leq; n and
1 &leq; j<sub>1</sub> < j<sub>2</sub> <  &ctdot; <  j<sub>p</sub> &leq; m
such that 
a<sub>i<sub>1</sub></sub>= b<sub>j<sub>1</sub></sub>, ..., a<sub>i<sub>p</sub></sub> = b<sub>j<sub>p</sub></sub>. 
The problem has applications in data comparison 
(e.g., diff utility, merge operation 
in various version control systems), 
bioinformatics (finding similarities 
between genes in various species), and others.
