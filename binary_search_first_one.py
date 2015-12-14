import random
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r %f sec' % \
              (method.__name__, te-ts)
        return result

    return timed


@timeit
def binary_search_first_one(array):
  low = 0
  high = len(array) - 1
  found = -1
  while high >= low:
    mid = (low + high) / 2
    if array[mid] == 1:
      found = mid
      high = mid - 1
    else:
      low = mid + 1
  return found


@timeit
def iter_search_first_one(array):
  for i in range(len(array)):
    if array[i] == 1:
      return i
  return -1


if __name__ == '__main__':
  array = list()
  for _ in range(10000):
    array.append(random.randint(0, 1))
  array.sort()
  print "binary: found at - {}".format(binary_search_first_one(array))
  print "regular: found at - {}".format(iter_search_first_one(array))
