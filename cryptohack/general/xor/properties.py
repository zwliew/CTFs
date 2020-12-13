k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k1xk2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2xk3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
k1xk2xk3xflag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


def solve():
    k1b = bytes.fromhex(k1)
    k2xk3b = bytes.fromhex(k2xk3)
    k1xk2xk3xflagb = bytes.fromhex(k1xk2xk3xflag)
    k1xflagb = bytes(x ^ y for x, y in zip(k2xk3b, k1xk2xk3xflagb))
    flag = "".join(chr(x ^ y) for x, y in zip(k1b, k1xflagb))
    return flag


print(solve())
