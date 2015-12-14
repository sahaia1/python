import sys

def gcd(m, n):
  if m > n:
    larger = m
    smaller = n
  else:
    smaller = m
    larger = n

  while True:
    if larger % smaller == 0:
      return smaller
    else:
      r = larger % smaller
      larger = smaller
      smaller = r

def euclid_gcd(a, b):
  if a > b:
    m = a
    n = b
  else:
    m = b
    n = a

  if n == 0:
    return m
  else:
    return euclid_gcd(n, m % n)

def diff_gcd(a, b):
  r = abs(a-b)
  if r == 0:
    return a
  else:
    a = min(a, b)
    b = r
    print "a - {} \t b - {}".format(a, b)
    return diff_gcd(a, b)

def euclid_extended(m, n, a=0, b=1, a_prime=1, b_prime=0):
  c = m
  d = n
  r = c % d
  q = c / d
  if r == 0:
    print "a = {} and b = {} and d = {}".format(a, b, d)
    return
  else:
    print "a_prime = {} and b_prime = {} and c = {}".format(a_prime, b_prime, c)
    c = d
    d = r
    t = a_prime
    a_prime = a
    a = t - q * a
    t = b_prime
    b_prime = b
    b = t - q * b
    return euclid_extended(c, d, a=a, b=b, a_prime=a_prime, b_prime=b_prime)


if __name__ == "__main__":
 # print gcd(int(sys.argv[1]), int(sys.argv[2]))
 # print euclid_gcd(int(sys.argv[1]), int(sys.argv[2]))
 # print diff_gcd(float(sys.argv[1]), float(sys.argv[2]))
  euclid_extended(int(sys.argv[1]), int(sys.argv[2]))
