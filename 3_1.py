def area(a, b, c):
	p = (a + b + c) / 2
	x = p * (p - a) * (p - b) * (p - c)
	s = x ** (0.5)
	return s