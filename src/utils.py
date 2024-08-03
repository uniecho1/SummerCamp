import random


def legendre_symbol(a, p):
    """Compute the Legendre symbol a|p using Euler's criterion.
    p is a prime, a is an integer.
    Returns 1 if a is a quadratic residue mod p, -1 if it is a non-quadratic residue, and 0 if a is 0 mod p.
    """
    ls = pow(a, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls


def modular_sqrt(a, p):
    """Find a quadratic residue (mod p) of 'a'.
    p must be an odd prime.
    Solve the congruence of the form:
        x^2 = a (mod p)
    And returns x. Note that p - x is also a root.
    Returns None if no square root exists for these a and p.
    """
    # Simple cases
    if legendre_symbol(a, p) != 1:
        return None
    elif a == 0:
        return 0
    elif p == 2:
        return a
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for odd s
    s, e = p - 1, 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Initialize variables
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def is_prime(n, k=30):
    """Test if a number is prime using the Miller-Rabin primality test.

    Args:
        n: The number to test.
        k: The number of test rounds to perform (default is 20).

    Returns:
        True if n is likely prime, False if n is composite.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d*2^r
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Witness loop
    def is_composite_witness(a):
        """Test if a is a composite witness for n."""
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    trylist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in trylist:
        if is_composite_witness(a):
            return False

    # Perform k tests
    for _ in range(k):
        a = random.randrange(38, n - 1)
        if is_composite_witness(a):
            return False

    return True


def random_string(len):
    string = ""
    for _ in range(len):
        string += chr(random.randint(32, 126))
    return string
