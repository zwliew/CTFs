orig = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
res = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hex_to_base64(x):
    import binascii

    ans = binascii.a2b_hex(x)
    ans = binascii.b2a_base64(ans)
    ans = ans.decode()
    ans = ans.strip()

    # Alternative using the codecs module
    # import codecs
    # ans = codecs.decode(orig, "hex")
    # ans = codecs.encode(ans, "base64")
    # ans = ans.decode()
    # ans = ans.strip()
    return ans


assert hex_to_base64(orig) == res
