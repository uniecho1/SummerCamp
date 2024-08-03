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

ECC_list = [ecnu32v1, secp256k1, secp521r1]


def build_mapping_table(EC: EllipticCurve):
    mapping_table = {}
    for c in range(32, 127):
        # print(f"{c} : {chr(c)}")
        # print(
        #     f"{chr(c)} : {EC.scalar_multiplication(random.randint(1, EC.p - 1), EC.get_g())}"
        # )
        mapping_table[chr(c)] = EC.scalar_multiplication(
            random.randint(1, EC.p - 1), EC.get_g()
        )
    return mapping_table


def Encrypt(message: str, EC: EllipticCurve, pk: tuple, r=None):
    algorithm = Algorithm(EC)
    point = User(EC).encode(message)
    return algorithm.encrypt(pk, point, r)


def make_single_data(id: int, len: int, EC: EllipticCurve):
    # mapping_table = build_mapping_table(EC)
    path = f"../test_data/test_{id}"
    message = utils.random_string(len)
    subprocess.run(["mkdir", path])
    # with open(f"{path}/mapping_table", "w") as f:
    #     for k, v in mapping_table.items():
    #         f.write(f"{k} : {v}\n")
    with open(f"{path}/message", "w") as f:
        f.write(message)
    with open(f"{path}/EllipticCurveGroup", "w") as f:
        f.write(str(EC))


def make_data(n=20):
    ratio = [0, 0.3, 0.6, 1]
    for i in range(len(ratio) - 1):
        for _ in range(int(ratio[i] * n), int(ratio[i + 1] * n)):
            make_single_data(_, random.randint(100, 1000), ECC_list[i])


make_data()
