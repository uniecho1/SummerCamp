from EllipticCurve import EllipticCurve
from Algorithm import Algorithm
from User import User
import utils
import random
import subprocess

ecnu32v1 = EllipticCurve(
    0,
    7,
    10**9 + 7,
)

secp256k1 = EllipticCurve(
    0,
    7,
    2**256 - 2**32 - 977,
    (
        55066263022277343669578718895168534326250603453777594175500187360389116729240,
        32670510020758816978083085130507043184471273380659243275938904335757337482424,
    ),
)

secp521r1 = EllipticCurve(
    -3,
    0x051953EB9618E1C9A1F929A21A0B68540EEA2DA725B99B315F3B8B489918EF109E156193951EC7E937B1652C0BD3BB1BF073573DF883D2C34F1EF451FD46B503F00,
    2**521 - 1,
    (
        0x00C6858E06B70404E9CD9E3ECB662395B4429C648139053FB521F828AF606B4D3DBAA14B5E77EFE75928FE1DC127A2FFA8DE3348B3C1856A429BF97E7E31C2E5BD66,
        0x011839296A789A3BC0045C8A5FB42C7D1BD998F54449579B446817AFBD17273E662C97EE72995EF42640C550B9013FAD0761353C7086A272C24088BE94769FD16650,
    ),
)

ECC_list = [(998244353, 3), ecnu32v1, secp256k1, secp521r1]


def build_mapping_table(Group):
    mapping_table = {}
    # r = random.sample(range(1, Group.p - 1), 127 - 32)
    r = []

    if type(Group).__name__ == "EllipticCurve":
        EC = Group
        for _ in range(127 - 32):
            tmp = random.randint(1, Group.p - 1)
            while tmp in r:
                tmp = random.randint(1, Group.p - 1)
            r.append(tmp)
        for c in range(32, 127):
            mapping_table[chr(c)] = EC.scalar_multiplication(r[c - 32], EC.get_g())
    else:
        p, g = Group
        for _ in range(127 - 32):
            tmp = random.randint(1, p - 1)
            while tmp in r:
                tmp = random.randint(1, p - 1)
            r.append(tmp)
        for c in range(32, 127):
            mapping_table[chr(c)] = pow(g, r[c - 32], p)
    return mapping_table


def Encrypt(message: str, mapping_table, Group, pk: tuple, r=None):
    CT = []
    if type(Group).__name__ == "EllipticCurve":
        EC = Group
        algorithm = Algorithm(EC)
        for c, o in zip(message, r):
            point = mapping_table[c]
            C = algorithm.encrypt(pk, point, o)
            CT.append(C)
    else:
        p, g = Group
        for c, o in zip(message, r):
            m = mapping_table[c]
            c1 = pow(g, o, p)
            c2 = (m * pow(pk, o, p)) % p
            CT.append((c1, c2))
    return CT


def make_single_data(id: int, len: int, Group):
    # print(type(Group).__name__=="EllipticCurve")

    message = utils.random_string(len)
    path = f"../test_data/test_{id}"
    subprocess.run(["mkdir", path])
    mapping_table = build_mapping_table(Group)
    if type(Group).__name__ == "EllipticCurve":
        EC = Group
        sk = random.randint(1, EC.p - 1)
        pk = EC.scalar_multiplication(sk, EC.get_g())
        # r = random.randint(1, EC.p - 1)
        r = [random.randint(1, EC.p - 1) for _ in range(message.__len__())]
        ciphertext = Encrypt(message, mapping_table, EC, pk, r)
        header = "EllipticCurve\n"
    else:
        p, g = Group
        sk = random.randint(1, p - 1)
        pk = pow(g, sk, p)
        # r = random.randint(1, p - 1)
        r = [random.randint(1, p - 1) for _ in range(message.__len__())]
        ciphertext = Encrypt(message, mapping_table, Group, pk, r)
        header = "Zp\n"
    output = header + message + "\n"
    output += str(Group) + "\n"
    output += f"({pk}, {sk})\n"
    output += str(r) + "\n"
    output += str(ciphertext) + "\n"
    with open(f"{path}/data", "w") as f:
        f.write(output)
    # with open(f"{path}/mapping_table", "w") as f:
    #     for k, v in mapping_table.items():
    #         f.write(f"{k} : {v}\n")
    # with open(f"{path}/message", "w") as f:
    #     f.write(message)
    # with open(f"{path}/Group", "w") as f:
    #     if type(Group).__name__ == "EllipticCurve":
    #         header = "EllipticCurve\n"
    #     else:
    #         header = "Zp\n"
    #     f.write(header + str(Group))
    # with open(f"{path}/parameter", "w") as f:
    #     f.write(f"pk : {pk}\nsk : {sk}\nr : {r}")
    # with open(f"{path}/ciphertext", "w") as f:
    #     f.write(f"{ciphertext}\n")


def make_data(n=50):
    ratio = [0, 0.2, 0.5, 0.8, 1]
    for i in range(len(ratio) - 1):
        for _ in range(int(ratio[i] * n), int(ratio[i + 1] * n)):
            make_single_data(_, random.randint(100, 1000), ECC_list[i])


make_data()
