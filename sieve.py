__author__ = 'webster'

def sieve(n):
    numbers = range(2, n + 1)
    for i in numbers:
        counter = 2
        while True:
            val = i * counter
            if val > n:
                break
            try:
                numbers.remove(val)
            except ValueError:
                pass
            counter += 1

    print numbers

sieve(1000)