orig = 11515195063862318899931685488813747395775516287289682636499965282714637259206269


def convert(x):
    b = bytearray()
    while x:
        b.append(x & 0xFF)
        x >>= 8
    b.reverse()
    b = bytes(b)
    return b


print(convert(orig))
