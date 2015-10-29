from Simulator import Simulator
from Estimators import eom_lee

if __name__ == '__main__':

	simulator = Simulator(initial_slots=10, simulations=10, min_tags=1, max_tags=1000, 
							step=100, estimator=eom_lee)


	# Use this to generate graphics
	result = simulator.run()

	print(result)
