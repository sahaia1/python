__author__ = "webster"

from time import sleep


def find_j(array, i, size, val):
  high = size - 1
  low = i
  while high - low > 1:
    mid = (high + low) / 2
    print "high - {} - low - {} - array mid - {}".format(high, low, array[mid])
    if array[mid] < val:
      high = mid
    elif array[mid] >= val:
      low = mid
  return high


def monkiness3(array1, array2, size):
  diffs = []
  for i in xrange(0, size):
     diffs.append(find_j(array2, i, size, array1[i]) - i)
     # print "{} - {} - {}".format(i, array1[i], find_j(array2, i, size, array1[i]))
  return max(diffs)


if __name__ == '__main__':
  num_inputs = int(raw_input())
  for _ in xrange(0, num_inputs):
    size = int(raw_input())
    array1 = [int(x) for x in raw_input().split()]
    array2 = [int(x) for x in raw_input().split()]
    print monkiness3(array1, array2, size)

