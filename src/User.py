import EllipticCurve


class User:
    def __init__(self, EC: EllipticCurve, x):
        self.EC = EC
        self.sk = x
        self.pk = self.EC.scalar_multiplication(x, self.EC.get_g())
