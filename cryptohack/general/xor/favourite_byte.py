encoded = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"


def solve(encoded):
    encoded = bytes.fromhex(encoded)
    key = encoded[0] ^ ord("c")
    decoded = [chr(x ^ key) for x in encoded]
    return "".join(decoded)


print(solve(encoded))
