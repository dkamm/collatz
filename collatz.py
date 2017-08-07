import numpy as np

def basen(n, b):
    """Returns a string of base b representation with LSB on LEFT."""
    ret = ''
    while n:
        r = n % b
        ret += str(r)
        n = n // b
    return ret

def base2(n):
    """Returns a string of base 2 representation with LSB on LEFT."""
    return basen(n, 2)

def base3(n):
    """Returns a string of base 3 representation with LSB on LEFT."""
    return basen(n, 3)

def successor(parent, i):
    """Returns the i'th successor of the parent."""
    if parent % 3 == 1:
        l = 2 * i
        pow_2 = 2 ** l
        return (pow_2 * parent - 1) // 3

    elif parent % 3 == 2:
        l = 2 * i + 1
        pow_2 = 2 ** l
        return (pow_2 * parent - 1) // 3
    else:
        return np.nan

def children(x, n=5):
    """Returns all of the numbers reachable to x in 1 step."""
    if x % 2 == 0:
        if x % 3 == 1:
            return [(x - 1) // 3]
        return []
    else:
        return [2 ** i * x for i in range(1, n + 1)]

def fromb(x, b):
    """Converts base b string into int val."""
    if b > 10:
        raise ValueError('base > 10 not supported')
    ret = 0
    for i in range(len(x)):
        ret += int(x[i]) * b ** i
    return ret


def from2(x):
    """Converts base2 string into int val."""
    return fromb(x, 2)


def from3(x):
    """Converts base3 string into int val."""
    return fromb(x, 3)


def isprime(x):
    """Returns true if x is prime."""
    for d in range(2, int(np.sqrt(x)) + 1):
        if x % d == 0:
            return False
    return True

def next(x):
    """Returns the next element in the collatz sequence."""
    if x == 1:
        return x
    elif x % 2 == 1:
        return 3 * x + 1
    else:
        return x // 2

def parent(x):
    """Returns the next odd number in the collatz sequence (parent in collatz tree)."""
    y = 3 * x + 1
    while not y % 2:
        y /= 2
    return y

def children(x, n):
    """Returns list of first n children of x."""
    if x % 3 == 0:
        return []
    elif x % 3 == 1:
        evens = [2 ** (2 * i) * x for i in range(1, n+1)]
        return [(x - 1) // 3 for x in evens]
    else:
        evens = [2 ** (2 * i + 1) * x for i in range(0, n)]
        return [(x - 1) // 3 for x in evens]


def ancestors(x):
    """Returns sequence of odd numbers in collatz sequence starting at x."""
    ret = []
    while x != 1:
        x = next(x)
        if x % 2 == 1:
            ret.append(x)
    return ret

def numsteps(n):
    """Returns the number of odd numbers visited in collatz process including the first if it is odd."""
    return len(ancestors(n))
