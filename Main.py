from Simulator import Simulator
from Estimators import lower_bound

if __name__ == '__main__':

	simulator = Simulator(initial_slots=10, min_tags=1, max_tags=1000, 
							step=100, estimator=lower_bound)


	# Use this to generate graphics
	result = simulator.run()

	print(result)
