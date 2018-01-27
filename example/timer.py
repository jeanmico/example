import numpy as np
from algs import quicksort, bubblesort
import matplotlib
from matplotlib import pyplot as plt
import timeit

def timetest():
	sizes = [10, 100, 200, 300, 500, 750, 1000, 2500, 5000]

	qtimes = []
	btimes = []

	qcond = []
	qasgn = []

	bcond = []
	basgn = []

	for count, size in enumerate(sizes):
		a = np.random.rand(100, size)

		qcond_tmp = []
		qasgn_tmp = []
		start_time = timeit.default_timer()
		for i in a:
			np.random.shuffle(i)
			(result, cond, asgn) = quicksort(i)
			qcond_tmp.append(cond)
			qasgn_tmp.append(asgn)
		qtimes.append(timeit.default_timer() - start_time)
		qcond.append(np.mean(qcond_tmp))
		qasgn.append(np.mean(qasgn_tmp))
		print(size)

		bcond_tmp = []
		basgn_tmp = []
		start_time = timeit.default_timer()
		for j in a:
			np.random.shuffle(j)
			(result, cond, asgn) = bubblesort(j)
			bcond_tmp.append(cond)
			basgn_tmp.append(asgn)
		btimes.append(timeit.default_timer() - start_time)
		bcond.append(np.mean(bcond_tmp))
		basgn.append(np.mean(basgn_tmp))
		print(size)

	with open("times.txt", "w+") as outfile:
		outfile.write(" ".join(str(x) for x in sizes))
		outfile.write("\n")
		outfile.write(" ".join(str(x) for x in qtimes))
		outfile.write("\n")
		outfile.write(" ".join(str(x) for x in btimes))

	with open("cond.txt", "w+") as outfile:
		outfile.write(" ".join(str(x) for x in sizes))
		outfile.write("\n")
		outfile.write(" ".join(str(x) for x in qcond))
		outfile.write("\n")
		outfile.write(" ".join(str(x) for x in bcond))
		outfile.write("\n")

	with open("asgn.txt", "w+") as outfile:
		outfile.write(" ".join(str(x) for x in sizes))
		outfile.write("\n")
		outfile.write(" ".join(str(x) for x in qasgn))
		outfile.write("\n")
		outfile.write(" ".join(str(x) for x in basgn))


timetest()
