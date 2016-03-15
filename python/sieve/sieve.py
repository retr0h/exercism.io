def sieve(num):
    return [g for g in generate_primes(num)]


def generate_primes(num):
    d = {}

    for n in range(2, num + 1):
        if n not in d:
            yield n
            d[n * n] = [n]
        else:
            for p in d[n]:
                d.setdefault(p + n, []).append(p)
            del d[n]
