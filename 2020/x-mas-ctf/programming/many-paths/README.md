# Many Paths [Programming - 500 points]

## Description

> Today in Santa's course in Advanced Graph Algorithms, Santa told us about the adjacency matrix of an undirected graph. I'm sure this last problem, he gave us is unsolvable, but I don't know much, maybe you do.
>
> Target: nc challs.xmas.htsp.ro 6053\
> Authors: Gabies, Nutu

## Solution

Upon connecting to the specified host, we see the following message:

> I swear that Santa is going crazy with those problems, this time we're really screwed!\
> The new problem asks us the following:\
> Given an undirected graph of size N by its adjacency matrix and a set of forbidden nodes, tell me how many paths from node 1 to node N of exactly length L that don't pass through any of the forbidden nodes exist (please note that a node can be visited multiple times)?\
> And if that wasn't enough, we need to answer 40 of those problems in 45 seconds and to give each output modulo 666013. What does that even mean!?\
> \
> Test number: 1/40\
> N = 3\
> adjacency matrix:\
> 0,1,1\
> 1,0,0\
> 1,0,0\
> forbidden nodes: []\
> L = 5

If you're familiar with graph theory, this is a pretty straightforward problem solved with matrix exponentiation.

Running [solution.py](./solution.py), pass all 50 stages and finally see the following message:

> b"I cannot believe you figured this one out, how does this code even work?\nI'm baffled, here's the flag: X-MAS{n0b0dy_3xp3c73d_th3_m47r1x_3xp0n3n71a7i0n}\n"

In conclusion, the flag is: `X-MAS{n0b0dy_3xp3c73d_th3_m47r1x_3xp0n3n71a7i0n}`.
