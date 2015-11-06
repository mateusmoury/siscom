import matplotlib.pyplot as plt
from QT import *
from QTSL import *
import sys

sys.setrecursionlimit(1000000)
#Number of tags for each experiment 
num_tags = ["100","200","300","400","500","600","700","800","900","1000"]


resQT = []
resQTSL = []
for x in num_tags:
	filename = "./benchmarks/" + x + "/" + x + ".txt"
	with open(filename) as inc:
		tags = []
		for line in inc:
			tags.append(line)	
		qt = QT(tags)
		ans = qt.run()
		resQT.append((x, ans['bits_sum']))
	
		qtsl = QTSL(tags)
		ans2 = qtsl.run()
		resQTSL.append((x, ans2['bits_sum']))

#Plotting

plt.figure(1)
plt.title('#Tags vs Bits Transmitidos - QT')
plt.scatter(*zip(*resQT))
plt.ylabel('Bits Transmitidos')
plt.xlabel('#Tags')
plt.show()


plt.figure(2)
plt.title('#Tags vs Bits Transmitidos - QTSL')
plt.scatter(*zip(*resQTSL))
plt.ylabel('Bits Transmitidos')
plt.xlabel('#Tags')
plt.show()
