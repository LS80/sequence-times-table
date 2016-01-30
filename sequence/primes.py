from itertools import count


def _is_prime(num):
    if num <= 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


def gen(n):
    ''' Generate n number of primes '''
    n = int(n)
    assert n > 0
    yield 2
    if n == 1:
        return
    i = 1
    for num in count(start=3, step=2):
        if _is_prime(num):
            yield num
            i += 1
            if i == n:
                return
