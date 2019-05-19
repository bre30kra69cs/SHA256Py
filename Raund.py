static_dict = {"a": 0x6a09e667, "b": 0xbb67ae85, "c": 0x3c6ef372, "d": 0xa54ff53a,
               "e": 0x510e527f, "f": 0x9b05688c, "g": 0x1f83d9ab, "h": 0x5be0cd19}
K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
     0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
     0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
     0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
     0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
     0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]


# Преобразование одного блока
def one_block_permutation(input_dict, M):
    H = input_dict
    W = W_gen(M)
    print("init", [hex(H[j]) for j in H.keys()])
    for i in range(64):
        T1 = (H["h"] + Zig1(H["e"]) + Ch(H["e"], H["f"], H["g"]) + K[i] + W[i]) % (2**32)
        T2 = (Zig0(H["a"]) + Maj(H["a"], H["b"], H["c"])) % (2**32)
        h = H["g"]
        g = H["f"]
        f = H["e"]
        e = (H["d"] + T1) % (2**32)
        d = H["c"]
        c = H["b"]
        b = H["a"]
        a = (T1 + T2) % (2**32)
        H = {"a": a, "b": b, "c": c, "d": d, "e": e, "f": f, "g": g, "h": h}
        print(i, [hex(H[j]) for j in H.keys()])
    return {"a": (input_dict["a"] + H["a"]) % (2**32), "b": (input_dict["b"] + H["b"]) % (2**32),
            "c": (input_dict["c"] + H["c"]) % (2**32), "d": (input_dict["d"] + H["d"]) % (2**32),
            "e": (input_dict["e"] + H["e"]) % (2**32), "f": (input_dict["f"] + H["f"]) % (2**32),
            "g": (input_dict["g"] + H["g"]) % (2**32), "h": (input_dict["h"] + H["h"]) % (2**32)}


def W_gen(M):
    W = M
    for j in range(16, 64): W.append((q1(W[j - 2]) + q0(W[j - 15]) + W[j - 7] + W[j - 16]) % (2**32))
    return W


def q0(x):
    return S(x, 7) ^ S(x, 18) ^ R(x, 3)


def q1(x):
    return S(x, 17) ^ S(x, 19) ^ R(x, 10)


def Zig0(x):
    return S(x, 2) ^ S(x, 13) ^ S(x, 22)


def Zig1(x):
    return S(x, 6) ^ S(x, 11) ^ S(x, 25)


def Ch(x, y, z):
    return (x & y) ^ (reverse(x) & z)


def Maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def R(value, rotation):
    return value >> rotation


def S(value, rotation):
    state_1 = create_right_word32(value)[len(create_right_word32(value)) - rotation:]
    state_2 = create_right_word32(value)[:len(create_right_word32(value)) - rotation]
    return int(state_1 + state_2, 2)


# Побитовый ревёрс(~) слова в 32 бита
def reverse(x):
    result = ""
    state = create_right_word32(x)
    for i in range(len(state)):
        if state[i] == "0": result += "1"
        else: result += "0"
    return int(result, 2)


# Организация правильного слова в 32 бита
def create_right_word32(input_int):
    return "".join(["0" for i in range(32 - len(bin(input_int)[2:]))]) + bin(input_int)[2:]