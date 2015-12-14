__author__ = "webster"


def last_occr(array, val):
  low = 0
  high = len(array) - 1
  while high - low > 1:
    mid = (high + low) / 2
    if array[mid] < val:
      high = mid
    else:
      low = mid

  return high


if __name__ == "__main__":
  array = [int(x) for x in raw_input().split()]
  array.sort(reverse=True)
  val = int(raw_input())
  print last_occr(array, val)
