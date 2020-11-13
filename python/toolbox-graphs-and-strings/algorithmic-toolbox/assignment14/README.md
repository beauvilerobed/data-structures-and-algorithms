# Primitive Calculator

Find the minimum number of operations 
needed to get a positive integer n from 1 
using only three operations: 
add 1, multiply by 2, and multiply by 3.

**Input.** An integer 1 &le; n &le; 10<sup>6</sup>.

**Output.** In the first line, output 
the minimum number k of operations needed to 
get n from 1. In the second line, 
output a sequence of intermediate numbers. 
That is, the second line should contain 
positive integers a<sub>0</sub>, a<sub>1</sub>, ... , a<sub>k</sub> 
such that a<sub>0</sub> = 1, a<sub>k</sub> = n, and 
for all 1 &le; i &le; k, a<sub>i</sub> is equal to 
either a<sub>i−1</sub> + 1, 2a<sub>i−1</sub>, or 3a<sub>i−1</sub>. 
If there are many such sequences, output any one of them.
