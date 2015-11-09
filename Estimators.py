from math import exp

def lower_bound(collisions, success, empty):
	return 2*collisions;

def eom_lee(collisions, success, empty):
	gama, beta, l = float(2), float('inf'), collisions + success + empty
	threshold = 0.001

	while True:
		new_beta = l / (gama * collisions + success)
		new_gama = (1 - exp(-1 / new_beta)) / (new_beta * (1 - (1 + 1 / new_beta) * exp(-1 / new_beta)))

		if (abs(new_gama - gama) < threshold):
			gama = new_gama
			break
		else:
			gama = new_gama
			beta = new_beta

	return int(gama * collisions)

def chen(collisions, success, empty):
	l = float(empty + success + collisions)
	n = float(success + 2 * collisions)
	next = 0.0
	previous = - 1.0
	while previous < next:
		p_e = (1.0 -  (1.0 / l)) ** n
		p_s = (n / l) * ((1.0 - (1.0 / l)) ** (n - 1.0))
		p_c = 1.0 - p_e - p_s
		previous = next
		next = fat(l, empty, success, collisions) * (p_e ** empty) * (p_s ** success) * (p_c ** collisions)
		n = n + 1.0
	n = n - 2.0
	return int(n)

def fat(a,b,c,d):
	res = 1.0
	a = float(a)
	b = float(b)
	c = float(c)
	d = float(d)
	while a > 1:
		res = res * a
		a = a - 1.0
		if b > 1:
			res = res / b
			b = b - 1.0
		if c > 1:
			res = res / c
			c = c - 1.0
		if d > 1:
			res = res / d
			d = d - 1.0
	return res
