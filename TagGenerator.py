from random import randint
import os

class TagGenerator:

	number_of_bits = 96

	def __init__(self, number_of_tags, file_path):
		self.number_of_tags = number_of_tags
		self.file_path = file_path

	def run(self):
		tags = set()
		while len(tags) < self.number_of_tags:
			tag = ""
			for i in range(self.number_of_bits):
				tag += str(randint(0,1))
			tags.add(tag)

		with open(self.file_path, "w") as textfile:
			textfile.write("\n".join(tags))

minimum_number_of_tags = 100
maximum_number_of_tags = 1000
number_of_simulations = 1000
step = 100

for number_of_tags in range(minimum_number_of_tags, maximum_number_of_tags+1, step):
	newpath = './tag_ids/' + str(number_of_tags) + '/'
	if not os.path.exists(newpath):
		os.makedirs(newpath)
		for simulation in range(1, number_of_simulations+1):
			TagGenerator(number_of_tags, newpath + str(simulation) + '.txt').run()




