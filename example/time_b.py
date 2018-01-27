from matplotlib import pyplot as plt
import os
import numpy as np
from scipy.stats import linregress

with open("times.txt") as infile:
	lines = infile.readlines()

sizes = list(int(x) for x in lines[0].split())
qsort = list(float(x) for x in lines[1].split())
bsort = list(float(x) for x in lines[2].split())

sizes_mod = list(x**2 for x in sizes)

slope, intercept, r_value, p_value, std_err = linregress(sizes_mod, bsort)

fig, ax = plt.subplots()
plt.plot(np.array(sizes_mod), intercept + slope*np.array(sizes_mod), 'r', label='fit: ' + str(r_value)[0:5], alpha=.3)
plt.scatter(sizes_mod, bsort, c="orange", label="bubblesort", alpha=.5)

ax.set_ylabel("seconds")
ax.set_xlabel("(array length)^2")
ax.set_title("Time to sort 100 arrays")
ax.legend()


plt.savefig("time_b.png", dpi=300)