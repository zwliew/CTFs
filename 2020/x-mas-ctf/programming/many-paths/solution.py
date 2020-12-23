import telnetlib

tn = telnetlib.Telnet("challs.xmas.htsp.ro", 6053)

MOD = 666013


def mat_mult(a, b, forbidden):
    N = len(a)
    res = [[0 for j in range(N)] for i in range(N)]
    for k in range(N):
        if k in forbidden:
            continue
        for i in range(N):
            for j in range(N):
                res[i][j] += a[i][k] * b[k][j]
                res[i][j] %= MOD
    return res


def solve(N, adj, forbidden, L):
    res = [[int(i == j) for j in range(N)] for i in range(N)]
    while L:
        if L % 2:
            res = mat_mult(res, adj, forbidden)
        adj = mat_mult(adj, adj, forbidden)
        L //= 2
    return res[0][N - 1]


num = b"0/40"
while num != b"40/40":
    tn.read_until(b"Test number: ")
    num = tn.read_until(b"\n")[:-1]
    tn.read_until(b"= ")
    N = int(tn.read_until(b"\n")[:-1])
    tn.read_until(b"\n")
    adj = []
    for i in range(N):
        line = [int(x) for x in tn.read_until(b"\n")[:-1].split(b",")]
        adj.append(line)

    tn.read_until(b"[")
    forbidden = tn.read_until(b"]\n")[:-2].split(b",")
    if forbidden and forbidden[0]:
        forbidden = set(int(x) - 1 for x in forbidden)
    else:
        forbidden = set()
    tn.read_until(b"= ")
    L = int(tn.read_until(b"\n")[:-1])

    ans = f"{solve(N, adj, forbidden, L)}\n".encode()
    tn.write(ans)
    tn.read_until(b"\n")
    res = tn.read_until(b"\n")
    if res != b"Good, thats right!\n":
        break

    print(f"Done {num}")

print(num)
if num == b"40/40":
    print(tn.read_all())
