import matplotlib.pyplot as plt
from QT import QT
#importar o QWT

if __name__ == '__main__':
	results_for_qt = {}
	results_for_qwt = {}

	for number_of_tags in range(100, 10001, 100):
		print("Rodando com numero de tags: " + str(number_of_tags))
		qt_bits_sum = 0
		qwt_bits_sum = 0
		for simulation in range(1, 1001):
			print("Rodando a simulacaoo: " + str(simulation))
			filename = './tag_ids/' + str(number_of_tags) + '/' + str(simulation) + '.txt'
			with open(filename, "r") as my_file:
				tags = []
				for line in my_file:
					tags.append(line)
				qt = QT(tags)
				ans_qt = qt.run()
				qt_bits_sum += ans_qt['bits_sum']
				# Fazer 18-20 para qwt
		qt_bits_sum_mean = float(qt_bits_sum) / 1000.0
		results_for_qt[number_of_tags] = qt_bits_sum_mean
		# Fazer 22-23 para qwt

#Plotting

	plt.figure()
	plt.grid()
	plt.title("#Tags vs Bits Transmitidos")
	plt.plot([x[0] for x in results_for_qt.items()], [x[1] for x in results_for_qt.items()], 'ro-', label="QT")
	# Plotar qwt - semelhante linhas 33
	# mas tem que mudar a cor (terceiro parametro)
	# pode botar um 'bo-' e o label tambem!
	plt.ylabel('Bits Transmitidos')
	plt.xlabel('#Tags')
	plt.legend()
	plot.show()






