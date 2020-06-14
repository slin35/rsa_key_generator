import random

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if pow(num, 1, 2) == 0 and pow(num, 1, 2) == 0:
        return False
    
    i = 5

    while pow(i, 2) <= num:
        if pow(num, 1, i) == 0 or pow(num, 1, i + 2) == 0:
            return False
        i += 6

    return True


def gcd(e: int, n: int) -> int:
    while n != 0:
        e, n = n, pow(e, 1, n)
    return e


def get_key_pair(p: int, q: int) -> tuple:
    n = p * q
    totient = (p - 1) * (q - 1)
    e = random.randrange(1, n)
    while gcd(e, n) != 1:
        e = random.randrange(1, n)

    d = modular_multiplicative_inverse(e, n)

    return ((e, n), (d, n))


# extended euclidean algorithm
def modular_multiplicative_inverse(e: int, n: int) -> int:
    x = 1
    y = 0
    m = n

    if m == 1:
        return 0

    while (e > 1):
        q = e // n
        tmp = n
        n = pow(e, 1, n)
        e = tmp
        tmp = y

        y = x - q * y
        x = tmp

    return x


def main():
    print(get_key_pair(11, 5))


if __name__ == '__main__':
    main()
   
