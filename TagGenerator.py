from random import randint

class TagGenerator:

	def __init__(self, number_of_tags, number_of_bits, file_path):
		self.number_of_tags = number_of_tags
		self.number_of_bits = number_of_bits
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

teste = TagGenerator(5, 3, './teste.txt')
teste.run()




