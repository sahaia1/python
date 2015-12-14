__author__ = "aditya"

import random


def binary_search_recursive(array, high, low, val):
  # print "Entering binary_search_recursive - high - {}, low - {}".format(high, low)
  if high < low:
    # value not found
    return None
  mid = low + (high - low) / 2
  # print "mid - {} array[mid] - {} and val - {}".format(mid, array[mid], val)
  if array[mid] == val:
    return mid
  elif array[mid] < val:
    return binary_search_recursive(array, high, mid + 1, val)
  elif array[mid] > val:
    return binary_search_recursive(array, mid - 1, low, val)


def binary_search_iterative(array, val):
  low = 0
  high = len(array) - 1
  while high >= low:
    mid = low + (high - low) / 2
    print "high = {} low = {} mid = {}".format(high, low, mid)
    if array[mid] == val:
      return mid
    elif array[mid] > val:
      high = mid - 1
    else:
      low = mid + 1
  return None

if __name__ == '__main__':
  array = list()
  for _ in range(100):
    array.append(random.randint(0, 1))

  array.sort()
  val = random.randint(0, 1)
  found = binary_search_recursive(array, len(array) - 1, 0, val)
  if found:
    print "recursive: Value found at pos - {}".format(found)
  else:
    print "recursive: Value not found"

  found2 = binary_search_iterative(array, val)
  if found2:
    print "iterative: value found at pos - {}".format(found)
  else:
    print "iterative: value not found"

  print val in array

