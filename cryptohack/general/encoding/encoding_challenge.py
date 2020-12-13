import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")


def json_recv():
    line = readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


import binascii, codecs

err = False
for i in range(100):
    received = json_recv()

    if "error" in received:
        err = True
        break

    t = received["type"]
    encoded = received["encoded"]
    decoded = None
    try:
        if t == "base64":
            decoded = binascii.a2b_base64(encoded).decode()
        elif t == "hex":
            decoded = bytes.fromhex(encoded).decode()
        elif t == "rot13":
            decoded = codecs.encode(encoded, "rot_13")
        elif t == "bigint":
            decoded = bytes.fromhex(encoded[2:]).decode()
        elif t == "utf-8":
            decoded = "".join(chr(x) for x in encoded)
    except:
        print(t, encoded, type(encoded))
        break

    json_send({"decoded": decoded})

if not err:
    received = json_recv()
    print(received)
