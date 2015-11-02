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
