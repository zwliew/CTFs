# col

Upon analyzing [col.c](./res/col.c), we find that a 20-byte string is taken as input to the binary. An int pointer `ip` is used to read the array, adding the values read to an integer `res`. The final value of the integer `res` is compared with the hexadecimal value `0x21DD09EC` to determine whether the flag should be read.

As we know, an `int` pointer reads 4 bytes at a time. The loop in the `check_password(const char *)` function hence reads a total of 20 bytes from the array, exactly the same size as the string taken as input for the binary.

What I've learnt is that reading a `char` array with an `int` pointer reads 4 bytes/characters from the array and simply concatenates the ASCII values together. On most standard platforms, the reads are done in little endian order.

Hence, we have to construct a hexadecimal string that is 20 characters long, such that the sum of each contiguous 4-byte substring equals to `0x21DD09EC`.

After a bit of thinking, I came up with the string "y\x5z\x1Dp\x1`\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1". Splitting the string up into 4-byte substrings, it is "y\x5z\x1D p\x1`\x1 \x1\x1\x1\x1 \x1\x1\x1\x1". As you can see, the first 2 substrings contain most of the weightage of the original value, while the remaining 2 substrings only contain `1`s.

The reason why we use `1`s for the rest of the characters is that null characters (`\0`) are reserved as string terminators, so they cannot be used as part of the string itself.

Passing the string as input to `col` using the `bash` built-in `printf` gives us the flags.
```bash
col@pwnable:~$ ./col $(printf 'y\x5z\x1Dp\x1`\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1\x1')
[flag is printed here]
```
