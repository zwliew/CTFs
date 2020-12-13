orig = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"
res = "746865206b696420646f6e277420706c6179"


def fixed_xor(a, b):
    import binascii

    a = binascii.a2b_hex(a)
    b = binascii.a2b_hex(b)
    ans = bytes([x ^ y for x, y in zip(a, b)])
    ans = binascii.b2a_hex(ans)
    ans = ans.decode()
    
    # Alternative solution using bitwise XOR on ints
    # a = int(a, 16)
    # b = int(b, 16)
    # ans = a ^ b
    # ans = format(ans, "x")
    return ans


assert fixed_xor(orig, key) == res
