"""

Given a number, find the total number of divisors of the factorial of the number.

Since the answer can be very large , Print answer modulo (( 10^9)+7).
"""
__author__ = "webster"

MAX_VAL = 50000
mod = pow(10, 9) + 7
sieve = []

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def power(p, n):
    val = 1
    sum = 0
    i = 2
    while val > 0:
        val = n / p
        sum += val
        p = pow(p, i)
        i += 1
    return sum

if __name__ == "__main__":
    for each in primes_sieve2(50000):
        sieve.append(each)

    num_inputs = int(raw_input())
    for _ in xrange(num_inputs):
        number = int(raw_input())
        dict = {}
        for each in sieve:
            if each > number:
                break
            dict[each] = power(each, number)
        ans = 1
        for each in dict.keys():
            ans *= (dict[each]+1) % mod
        print ans % mod



