from Simulator import Simulator
from Estimators import *
import matplotlib.pyplot as plt

if __name__ == '__main__':

	simulator = Simulator(initial_slots=64, simulations=1, min_tags=100, max_tags=1000,
							step=100, estimator=eom_lee)


	# Use this to generate graphics
	result = simulator.run()

	print(result)
	
	# Generating Collisions vs Tags
	plt.figure(1)
	plt.title('Collisions vs Tags')
	plt.plot([x['tags'] for x in result], [x['collisions'] for x in result], 'r--')
	plt.ylabel('Collisions')
	plt.xlabel('Tags')
	
	# Generating Empty vs Tags
	plt.figure(2)
	plt.title('Empty vs Tags')
	plt.plot([x['tags'] for x in result], [x['empty'] for x in result], 'r--')
	plt.ylabel('Empty')
	plt.xlabel('Tags')
	plt.show()
