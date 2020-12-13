orig = "label"


def convert(s):
    ans = bytes(s, "utf-8")
    ans = bytes(x ^ 13 for x in ans)
    ans = ans.decode()
    return ans


print(convert(orig))
