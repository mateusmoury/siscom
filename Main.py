from Simulator import Simulator
from Estimators import *
import matplotlib.pyplot as plt
import time

if __name__ == '__main__':


	lb = Simulator(initial_slots=64, simulations=500, min_tags=100, max_tags=1000,
							step=100, estimator=lower_bound)

	lee = Simulator(initial_slots=64, simulations=500, min_tags=100, max_tags=1000,
							step=100, estimator=eom_lee)

	chen = Simulator(initial_slots=64, simulations=500, min_tags=100, max_tags=1000,
							step=100, estimator=chen)


	# Use this to generate graphics
	start_time = time.time()

	lb_result = lb.run()
	print("Tempo para execucao do lower bound: " + str(time.time() - start_time))

	start_time = time.time()

	lee_result = lee.run()
	print("Tempo de execucao do eom lee: " + str(time.time() - start_time))

	start_time = time.time()

	chen_result = chen.run()
	print("Tempo de execucao do chen: " + str(time.time() - start_time))

	print(lb_result)
	print(lee_result)
	print(chen_result)
	
	# Generating Collisions vs Tags
	plt.figure(1)
	plt.title('Collisions vs Tags')
	plt.plot([x['tags'] for x in lb_result], [x['collisions'] for x in lb_result], 'ro-', label="Lower Bound")
	plt.plot([x['tags'] for x in lee_result], [x['collisions'] for x in lee_result], 'bo-', label="Eom Lee")
	plt.plot([x['tags'] for x in chen_result], [x['collisions'] for x in chen_result], 'yo-', label="Chen")
	plt.ylabel('Collisions')
	plt.xlabel('Tags')
	plt.legend()
	
	# Generating Empty vs Tags
	plt.figure(2)
	plt.title('Empty vs Tags')
	plt.plot([x['tags'] for x in lb_result], [x['empty'] for x in lb_result], 'ro-', label="Lower Bound")
	plt.plot([x['tags'] for x in lee_result], [x['empty'] for x in lee_result], 'bo-', label="Eom Lee")
	plt.plot([x['tags'] for x in chen_result], [x['empty'] for x in chen_result], 'yo-', label="Chen")
	plt.ylabel('Empty')
	plt.xlabel('Tags')
	plt.legend()

	# Generating Slots vs Tags
	plt.figure(3)
	plt.title('Slots vs Tags')
	plt.plot([x['tags'] for x in lb_result], [x['slots'] for x in lb_result], 'ro-', label="Lower Bound")
	plt.plot([x['tags'] for x in lee_result], [x['slots'] for x in lee_result], 'bo-', label="Eom Lee")
	plt.plot([x['tags'] for x in chen_result], [x['slots'] for x in chen_result], 'yo-', label="Chen")
	plt.ylabel('Slots')
	plt.xlabel('Tags')
	plt.legend()

	# Generating Slots vs Tags
	# plt.figure(4)
	# plt.title('Avg. abs. error vs Tags')
	# plt.plot([x['tags'] for x in lb_result], [x['estimated'] for x in lb_result], 'ro-', label="Lower Bound")
	# plt.plot([x['tags'] for x in lee_result], [x['estimated'] for x in lee_result], 'bo-', label="Eom Lee")
	# plt.ylabel('Avg. Abs. Error')
	# plt.xlabel('Tags')
	# plt.legend()

	plt.show()