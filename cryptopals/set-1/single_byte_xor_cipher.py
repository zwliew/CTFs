from binascii import b2a_hex


orig = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def single_byte_xor_cipher(x):
    import collections
    import binascii

    weights = collections.defaultdict(
        lambda: 0,
        {
            "e": 11.2,
            "a": 8.5,
            "r": 7.6,
            "i": 7.5,
            "o": 7.1,
            "t": 7.0,
            "n": 6.7,
            "s": 5.7,
            "l": 5.5,
            "c": 4.5,
            "u": 3.6,
            "d": 3.4,
            "p": 3.2,
            "m": 3.0,
            "h": 3.0,
            "g": 2.5,
            "b": 2.1,
            "f": 1.8,
            "y": 1.8,
            "w": 1.1,
            "v": 0.3,
            "z": 0.3,
            "j": 0.2,
            "q": 0.2,
        },
    )

    def ok(s):
        for c in s:
            if not c.isprintable() and c != "\n":
                return False
        return True

    nums = binascii.a2b_hex(x)
    candidates = [("".join(chr(c ^ i) for c in nums)) for i in range(256)]
    candidates = [
        (s, sum(weights[c.lower()] for c in s) if ok(s) else float("-inf"))
        for s in candidates
    ]
    return max(candidates, key=lambda c: c[1])[0]


print(single_byte_xor_cipher(orig))
