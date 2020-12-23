# Biggest Lowest [Programming - 50 points]

## Description

> I see you're eager to prove yourself, why not try your luck with this problem?
>
> Target: nc challs.xmas.htsp.ro 6051\
> Authors: Gabies, Nutu

## Solution

Upon connecting to the host, we see the following message:

> So you think you have what it takes to be a good programmer?\
> Then solve this super hardcore task:\
> Given an array print the first k1 smallest elements of the array in increasing order and then the first k2 elements of the array in decreasing order.\
> You have 50 tests that you'll gave to answer in maximum 45 seconds, GO!\
> Here's an example of the format in which a response should be provided:\
> 1, 2, 3; 10, 9, 8
>
> Test number: 1/50\
> array = [5, 2, 7, 7, 2]\
> k1 = 1\
> k2 = 2

This is a simple automation task involving sorting and connecting to the host. I use `telnetlib`, but various other libraries like `pwntools` or `nclib` should work as well.

The idea is to sort the array and output the first `k1` elements and the last `k2` elements. See [solution.py](./solution.py) for the script used to solve this.

After completing all 50 stages, we see the following message:

> b"Those are some was lightning quick reflexes you've got there!\n Here's your flag: X-MAS{th15_i5_4_h34p_pr0bl3m_bu7_17'5_n0t_4_pwn_ch41l}\n"

Thus, the flag is `X-MAS{th15_i5_4_h34p_pr0bl3m_bu7_17'5_n0t_4_pwn_ch41l}`.
