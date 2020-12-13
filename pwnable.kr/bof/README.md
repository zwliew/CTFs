# bof

Dumping the object file with `objdump` and analyzing the assembly code of the `func` function at address `0x62c`, we can see that the `overflowme` character array is stored at the memory address `ebp - 0x2c`, while the integer compared which "0xcafebabe" is compared against is stored at `ebp + 0x8`.

Hence, we should write a total of `0x2c + 0x8 + 4` bytes, with the last 4 bytes being `0xcafebabe`.

[exploit.py](exploit.py) contains the exploit.
