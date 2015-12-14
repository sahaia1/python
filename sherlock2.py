def binary_search(array, size, val):
	high = size - 1
	low = 0
	while high >= low:
		mid = (high + low) / 2
		if array[mid] == val:
			return mid
		elif array[mid] > val:
			high = mid - 1
		else:
			low = mid + 1
	return mid

if __name__ == '__main__':
	k = [3, 4, 6, 7, 8, 9]
	val = 5
	print binary_search(k, len(k), val) 