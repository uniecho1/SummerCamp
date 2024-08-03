import EllipticCurve
import random


class Algorithm:
    def __init__(self, EC: EllipticCurve):
        self.EC = EC

    def encrypt(self, pk, point, r=None):
        if r is None:
            r = random.randint(1, self.EC.p - 1)
        C1 = self.EC.scalar_multiplication(r, self.EC.get_g())
        C2 = self.EC.point_addition(point, self.EC.scalar_multiplication(r, pk))
        return (C1, C2)

    def decrypt(self, sk, C):
        C1, C2 = C
        return self.EC.point_subtraction(C2, self.EC.scalar_multiplication(sk, C1))
