# fd

Upon analyzing [fd.c](./res/fd.c), we see that the hexadecimal value 0x1234 is subtracted from the only argument passed to the binary. Then, resulting value is used as a file descriptor from which 32 bytes are read into a `buf` character array. Based on the code, "LETMEWIN" should be read into `buf` in order for the flag to be printed.

As we know, the 3 main file descriptor values in Linux are:
- stdout (file descriptor 0)
- stdin (file descriptor 1)
- stderr (file descriptor 2)

Naturally, we want to use stdin to input the string "LETMEWIN" via `stdin`. Hence, we need a decimal value `x` such that `x - 0x1234 == 1`. Using a [hexadecimal to decimal converter](https://www.rapidtables.com/convert/number/hex-to-decimal.html), we get `0x1234 == 4660 (decimal)`. Hence, `x == 4661`.

Passing `4661` as the only argument to `fd` and inputting "LETMEWIN" via `stdin` prints the flag.

```bash
fd@pwnable:~$ ./fd 4661
LETMEWIN
[flag is printed here]
```
