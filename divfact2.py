"""
Factorial numbers are getting big very soon, you'll have to compute the number of divisors of such highly composite numbers.

Input

The first line contains an integer T, the number of test cases.
On the next T lines, you will be given two integers N and M.
Output

Output T lines, one for each test case, with the number of divisors of the factorial of N.
Since the answer can get very big, output it modulo M.
"""
__author__ = "webster"

MAX_VAL = pow(10, 9)
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
    for each in primes_sieve2(MAX_VAL):
        sieve.append(each)
    print "hello world"
    num_inputs = int(raw_input())
    for _ in xrange(num_inputs):
        number, mod = (int(x) for x in raw_input().split())
        dict = {}
        for each in sieve:
            if each > number:
                break
            dict[each] = power(each, number)
        ans = 1
        for each in dict.keys():
            ans *= (dict[each]+1) % mod
        print ans % mod



