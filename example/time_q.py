from matplotlib import pyplot as plt
import os
import numpy as np
from scipy.stats import linregress
from math import log

with open("times.txt") as infile:
	lines = infile.readlines()

sizes = list(int(x) for x in lines[0].split())
qsort = list(float(x) for x in lines[1].split())

sizes_mod = list(x*log(x) for x in sizes)

slope, intercept, r_value, p_value, std_err = linregress(sizes_mod, qsort)

fig, ax = plt.subplots()
plt.plot(np.array(sizes_mod), intercept + slope*np.array(sizes_mod), 'r', label='fit: ' + str(r_value)[0:5], alpha=.3)
plt.scatter(sizes_mod, qsort, c="blue", label="quicksort", alpha=.5)

ax.set_ylabel("seconds")
ax.set_xlabel("N log(N)")
ax.set_title("Time to sort 100 arrays")
ax.legend()


plt.savefig("time_q.png", dpi=300)