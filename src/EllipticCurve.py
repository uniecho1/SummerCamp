import utils
import random


class EllipticCurve:
    # y ^ 2 = x ^ 3 + a * x +b
    def __init__(self, a, b, p, g=None):
        self.a = a
        self.b = b
        self.p = p
        if g is None:
            self.g = self.gen_point()
        else:
            assert self.on_curve(g)
            self.g = g

    def get_g(self):
        return self.g

    def __str__(self):
        return f"y^2 = x^3 + {self.a}x + {self.b} (mod {self.p})\nG = {self.g}"

    def on_curve(self, point):
        """Check if the point (x, y) is on the curve."""
        x, y = point
        return (y**2 - x**3 - self.a * x - self.b) % self.p == 0

    def point_addition(self, P, Q):
        """Add two points P and Q on the elliptic curve."""
        if P == (None, None):
            return Q
        if Q == (None, None):
            return P

        x1, y1 = P
        x2, y2 = Q

        if x1 == x2 and y1 != y2:
            return (None, None)

        if P != Q:
            m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        else:
            try:
                m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p) % self.p
            except ValueError:
                # print("tag_uniecho1", 2 * y1 % self.p)
                return (None, None)

        x3 = (m**2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p

        return (x3, y3)

    def scalar_multiplication(self, k, P):
        """Multiply point P by an integer k."""
        R = (None, None)
        N = P

        while k:
            if k & 1:
                R = self.point_addition(R, N)
            N = self.point_addition(N, N)
            k >>= 1

        return R

    def point_negation(self, P):
        """Negate point P on the elliptic curve."""
        if P == (None, None):
            return P
        x, y = P
        return (x, -y % self.p)

    def point_subtraction(self, P, Q):
        """Subtract point Q from point P on the elliptic curve."""
        neg_Q = self.point_negation(Q)
        return self.point_addition(P, neg_Q)

    def gen_point(self):
        """Generate a random point on the elliptic curve."""
        x = random.randint(2, self.p - 1)
        y_square = (x**3 + self.a * x + self.b) % self.p
        while not utils.legendre_symbol(y_square, self.p) == 1:
            x = random.randint(0, self.p - 1)
            y_square = (x**3 + self.a * x + self.b) % self.p
        return (x, utils.modular_sqrt(y_square, self.p))


# while True:
#     EC = EllipticCurve(0, 7, 13)
#     x = EC.gen_point()
#     y = EC.gen_point()
#     assert EC.on_curve(x)
#     assert EC.on_curve(y)
#     z = EC.point_addition(x, y)
#     x_ = EC.point_subtraction(z, y)
#     print(x, y, z, x_)
#     assert x_ == x
