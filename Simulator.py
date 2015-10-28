from Simulation import Simulation

class Simulator:

	def __init__(self, initial_slots, simulations, min_tags, max_tags, step, estimator):
		self.initial_slots = initial_slots
		self.min_tags = min_tags
		self.max_tags = max_tags
		self.step = step
		self.estimator = estimator
		self.simulations = simulations

	def run(self):
		simulations = []

		for i in range(self.min_tags, self.max_tags+1, self.step):
			result = {
				'collisions': 0,
				'empty': 0,
				'success': 0,
				'tags': 0
			}

			for j in range(self.simulations):
				simulation = Simulation(self.initial_slots, i, self.estimator).run()
				result['collisions'] = result['collisions'] + simulation['collisions']
				result['empty'] = result['empty'] + simulation['empty']
				result['success'] = result['success'] + simulation['success']
				result['tags'] = result['tags']
			
			result['collisions'] = result['collisions'] / self.simulations;
			result['empty'] = result['empty'] / self.simulations;
			result['success'] = result['success'] / self.simulations;
			simulations.append(result)

		return simulations
