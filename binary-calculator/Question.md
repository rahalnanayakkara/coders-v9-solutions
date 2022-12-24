# Binary Calculator

## Problem Statement

Sudam is building a binary calculator. He wants to be able to multiply numbers by powers of $2$. Both the input and output to this calculator is in binary.

You are given the input number $x$ in binary, and a decimal integer $i$. Print the answer in binary, when $x$ is multiplied by $2^i$.

## Input Format

The first line contains a binary number $x$ (only $1$ and $0$)

The next line contains an integer $i$.

## Constraints

$x \leq 10^{12}$

$i \leq 10^{4}$

## Output Format

A single binary number (only $1$ and $0$), with no spaces

## Sample Input 0

```
1001
2
```

## Sample Output 0

```
100100
```

## Explanation 0

The number $n$ is $1001_2 = 9_{10}$

Given $i$ value is $2$. Therefore, the multiplication factor is $2^2 = 4$.

The answer will be $9 \times 4 = 36$

$36_{10} = 100100_2$

Therefore print "$100100$".