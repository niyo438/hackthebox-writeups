import struct
import ctypes

def rol(v, r):
    r &= 7
    return ((v << r) | (v >> (8 - r))) & 0xff

def ror(v, r):
    r &= 7
    return ((v >> r) | ((v << (8 - r)) & 0xff)) & 0xff

def decrypt(path):
    # Load libc for srand()/rand()
    libc = ctypes.CDLL("libc.so.6")
    srand = libc.srand
    rand = libc.rand
    srand.argtypes = [ctypes.c_uint]
    rand.restype = ctypes.c_int

    # Read file: first 4 bytes = seed, rest = ciphertext
    data = open(path, "rb").read()
    seed = struct.unpack("<I", data[:4])[0]
    ct = data[4:]

    # Init PRNG
    srand(seed)

    # Decrypt loop
    pt = bytearray(len(ct))
    for i, c in enumerate(ct):
        r1 = rand() & 0xff
        r2 = rand() & 7
        pt[i] = ror(c, r2) ^ r1

    return pt

if __name__ == "__main__":
    flag = decrypt("flag.enc")
    print("Decrypted:", flag.decode())
