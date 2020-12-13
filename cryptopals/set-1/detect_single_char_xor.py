def single_byte_xor_cipher(x):
    import collections
    import re
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
    candidates = [(x, i, "".join(chr(c ^ i) for c in nums)) for i in range(256)]
    candidates = [
        (
            s[0],
            s[1],
            s[2],
            sum(weights[c.lower()] for c in s[2]) if ok(s[2]) else float("-inf"),
        )
        for s in candidates
    ]
    ans = max(candidates, key=lambda c: c[3])
    return ans


def detect_single_char_xor():
    with open("input.txt") as f:
        candidates = [single_byte_xor_cipher(l.strip()) for l in f]
        return max(candidates, key=lambda c: c[3])[2]


print(detect_single_char_xor())
