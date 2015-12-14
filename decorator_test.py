from datetime import datetime
from dis import dis


def timer(func):
  def wrapper(*args, **kwargs):
    t1 = datetime.now()
    func(*args, **kwargs)
    t2 = datetime.now()
    print "time taken {}".format(t2-t1)
  return wrapper


@timer
def print_hello(text):
  print "text = {}".format(text)

@timer
def compute(a, b):
  return a + b

# print_hello("aditya")
c = compute(4, 5)
dis(compute)