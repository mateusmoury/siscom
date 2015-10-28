import random

class Simulation:

	def __init__(self, initial_slots, tags, estimator):
		self.initial_slots = initial_slots
		self.tags = tags
		self.estimator = estimator
		
		
	def run(self):
		tags_remaining = self.tags

		slots = self.initial_slots

		total_collisions = 0
		total_empty = 0
		total_success = 0

		while tags_remaining > 0:

			frame = [0 for i in range(slots)]
			
			# Randomly distributes tags for the slots
			for i in range(tags_remaining):
				r = random.randint(0, slots-1)
				frame[r] = frame[r] + 1

			collisions = 0
			success = 0
			empty = 0

			for slot in frame:
				if slot == 0:
					empty = empty + 1
					total_empty = total_empty + 1
				elif slot == 1:
					tags_remaining = tags_remaining - 1
					success = success + 1
					total_success = total_success + 1
				else:
					collisions = collisions + 1
					total_collisions = total_collisions + 1

			slots = self.estimator(collisions=collisions, success=success, empty=empty)

		return {
			'tags': self.tags,
			'collisions': total_collisions,
			'success': total_success,
			'empty': total_empty
		}

