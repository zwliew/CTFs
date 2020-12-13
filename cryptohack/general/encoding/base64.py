orig = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"


def convert(h):
    import binascii

    b = binascii.unhexlify(h)
    b64 = binascii.b2a_base64(b)
    return b64


print(convert(orig))
