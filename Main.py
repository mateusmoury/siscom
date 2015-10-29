from Simulator import Simulator
from Estimators import eom_lee

if __name__ == '__main__':

	simulator = Simulator(initial_slots=64, simulations=2000, min_tags=100, max_tags=1000,
							step=100, estimator=eom_lee)


	# Use this to generate graphics
	result = simulator.run()

	print(result)
