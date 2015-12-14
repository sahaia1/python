tc = int(raw_input())
while tc>0:
	tc = tc - 1
	curMax = 0
	n = int(raw_input())
	x = map(int, raw_input().split())
	y = map(int, raw_input().split())
  for i in xrange(n):
    low, high, pos = 0, n - 1, -1
    while low <= high:
      mid = (low + high) / 2
      if y[mid] >= x[i]:
        pos = mid
        low = mid + 1
      else:
        high = mid - 1
  curMax = max(curMax, pos - i)
  print curMax