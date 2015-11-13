import matplotlib.pyplot as plt
from QT import QT
from QWT import QWT
import time

if __name__ == '__main__':
	results_for_qt, results_for_qwt = [], []

	number_of_simulations = 1000

	for number_of_tags in range(100, 1001, 100):
		qt_bits_sum, qt_reader_bits_sum, qt_steps = 0, 0, 0
		qwt_bits_sum, qwt_reader_bits_sum, qwt_steps = 0, 0, 0
		for simulation in range(1, number_of_simulations + 1):
			filename = './tag_ids/' + str(number_of_tags) + '/' + str(simulation) + '.txt'
			with open(filename, "r") as my_file:
				tags = []
				for line in my_file:
					tags.append(line)

				qt = QT(tags)
				ans_qt = qt.run()

				qt_bits_sum += ans_qt['bits_sum']
				qt_reader_bits_sum += ans_qt['reader_bits_sum']
				qt_steps += ans_qt['steps']

				qwt = QWT(tags)
				ans_qwt = qwt.run()

				qwt_bits_sum += ans_qwt['bits_sum']
				qwt_reader_bits_sum += ans_qwt['reader_bits_sum']
				qwt_steps += ans_qwt['steps']

		qt_bits_sum_mean = float(qt_bits_sum) / number_of_simulations
		qt_reader_bits_sum_mean = float(qt_reader_bits_sum) / number_of_simulations
		qt_steps_mean = float(qt_steps) / number_of_simulations

		qwt_bits_sum_mean = float(qwt_bits_sum) / number_of_simulations
		qwt_reader_bits_sum_mean = float(qwt_reader_bits_sum) / number_of_simulations
		qwt_steps_mean = float(qwt_steps) / number_of_simulations

		results_for_qt.append([number_of_tags, qt_bits_sum_mean, qt_reader_bits_sum_mean, qt_steps_mean])
		results_for_qwt.append([number_of_tags, qwt_bits_sum_mean, qwt_reader_bits_sum_mean, qwt_steps_mean])

#Plotting

	plt.figure(1)
	plt.grid()
	plt.title("#Tags vs Bits Transmitidos Por Tag")
	plt.plot([x[0] for x in results_for_qt], [x[1] for x in results_for_qt], 'ro-', label="QT")
	plt.plot([x[0] for x in results_for_qwt], [x[1] for x in results_for_qwt], 'bo-', label="QWT")
	plt.ylabel('Bits Transmitidos por Tags')
	plt.xlabel('#Tags')
	plt.legend()

	plt.figure(2)
	plt.grid()
	plt.title("#Tags vs Bits Transmitidos Pelo Leitor")
	plt.plot([x[0] for x in results_for_qt], [x[2] for x in results_for_qt], 'ro-', label="QT")
	plt.plot([x[0] for x in results_for_qwt], [x[2] for x in results_for_qwt], 'bo-', label="QWT")
	plt.ylabel('Bits Transmitidos pelo Leitor')
	plt.xlabel('#Tags')
	plt.legend()

	plt.figure(3)
	plt.grid()
	plt.title("#Tags vs Numero de passos")
	plt.plot([x[0] for x in results_for_qt], [x[3] for x in results_for_qt], 'ro-', label="QT")
	plt.plot([x[0] for x in results_for_qwt], [x[3] for x in results_for_qwt], 'bo-', label="QWT")
	plt.ylabel('Numero de passos')
	plt.xlabel('#Tags')
	plt.legend()

	plt.show()






