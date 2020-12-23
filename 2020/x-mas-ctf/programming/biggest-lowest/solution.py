import telnetlib

url = ("challs.xmas.htsp.ro", 6051)
tn = telnetlib.Telnet(url[0], url[1])

status = b"0/50"
while status != b"50/50":
    tn.read_until(b"Test number: ")
    status = tn.read_until(b"\n")[:-1]
    tn.read_until(b"array = [")
    arr = tn.read_until(b"]\n")[:-2]
    arr = list(map(int, arr.split(b", ")))
    tn.read_until(b"k1 = ")
    ik = tn.read_until(b"\n")[:-1]
    ik = int(ik)
    tn.read_until(b"k2 = ")
    dk = tn.read_until(b"\n")[:-1]
    dk = int(dk)

    arr.sort()
    ans = ""
    for i in range(ik):
        if i:
            ans += ", "
        ans += str(arr[i])
    ans += "; "
    for i in range(len(arr) - 1, len(arr) - dk - 1, -1):
        if i < len(arr) - 1:
            ans += ", "
        ans += str(arr[i])

    tn.write(ans.encode() + b"\n")
    res = tn.read_until(b"\n")

    if res != b"Good, that's right!\n":
        break

if status == b"50/50":
    print(tn.read_all())
