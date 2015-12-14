large_num = pow(10, 9) + 7


def factorial(num):
	if num == 1 or num == 0:
		return 1
	else:
		return num * factorial(num - 1)

def new_mul(a, b1 ,b2):
	product1 = 1
	while a > b2:
		product1 = product1 * a
		a = a - 1
		if b1 > 0 and product1 % b1 == 0:
			product1 = product1 / b1
			b1 -= 1
	if b1 > 0:
		product2 = factorial(b1)
	else:
		product2 = 1
	return product1 / product2

def combinations(a, b):
	b1 = b
	b2 = a - b
	if b2 > b1:
		return new_mul(a, b2, b1)
	else:
		return new_mul(a, b1, b2)

if __name__ == '__main__':
	num_inputs = int(raw_input())
	for _ in xrange(num_inputs):
		num = int(raw_input())
		sum = 1
		index = 1
		for i in range(1, num):
			sum += combinations(num - 1, i) % large_num
			index += 1
		print sum % large_num