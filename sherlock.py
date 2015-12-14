__author__ = "webster"


if __name__ == '__main__':
	num_inputs = int(raw_input())
	for _ in xrange(num_inputs):
		n, k, p = (int(x) for x in raw_input().split())
		k_list = [int(y) for y in raw_input().split()]
		if p > (n - k):
			print "-1"
			continue
		else:
			index = 0
			for c in k_list:
				if c <= p:
					p += 1
			print p
