from Simulation import Simulation

class Simulator:

	def __init__(self, initial_slots, min_tags, max_tags, step, estimator):
		self.initial_slots = initial_slots
		self.min_tags = min_tags
		self.max_tags = max_tags
		self.step = step
		self.estimator = estimator

	def run(self):
		simulations = []

		for i in range(self.min_tags, self.max_tags+1, self.step):
			simulation = Simulation(self.initial_slots, i, self.estimator).run()
			simulations.append(simulation)

		return simulations
