import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import sys
import copy
sys.setrecursionlimit(20001)
import sorting_algo

very_start_time = time.time()

# Define test sizes, # of iterations, and max_value of each arr
test_sizes = [50, 100, 1000, 10000]
num_iterations = 10
max_value = 1000

# Define the sorting algorithms
sorting_algos = ['Bubble', 'Insertion', 'Merge', 'Quick']

# Initialize an empty DataFrame
df = pd.DataFrame(columns=test_sizes, index=sorting_algos)

for size in test_sizes:
	
	bubble_min_time = float('inf')
	bubble_max_time = float('-inf')
	insertion_min_time = float('inf')
	insertion_max_time = float('-inf')
	merge_min_time = float('inf')
	merge_max_time = float('-inf')
	quick_min_time = float('inf')
	quick_max_time = float('-inf')

	for i in range(num_iterations):
	
		random_array = [random.randint(0, max_value) for _ in range(size)]
		
		#Sort the array
		random_array.sort()
		
		random_array_copy = copy.deepcopy(random_array)
		
		start_time = time.time()
		sorting_algo.bubble_sort(random_array_copy)
		end_time = time.time()
		bubble_time = end_time - start_time
		bubble_time = round(bubble_time, 5)
		if bubble_time < bubble_min_time:
			bubble_min_time = bubble_time
		if bubble_time > bubble_max_time:
			bubble_max_time = bubble_time

		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.insertion_sort(random_array_copy)
		end_time = time.time()
		insertion_time = end_time - start_time
		insertion_time = round(insertion_time, 5)
		if insertion_time < insertion_min_time:
			insertion_min_time = insertion_time
		if insertion_time > insertion_max_time:
			insertion_max_time = insertion_time

		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.merge_sort(random_array_copy)
		end_time = time.time()
		merge_time = end_time - start_time
		merge_time = round(merge_time, 5)
		if merge_time < merge_min_time:
			merge_min_time = merge_time
		if merge_time > merge_max_time:
			merge_max_time = merge_time

		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.quick_sort(random_array_copy, 0, size - 1)
		end_time = time.time()
		quick_time = end_time - start_time
		quick_time = round(quick_time, 5)
		if quick_time < quick_min_time:
			quick_min_time = quick_time
		if quick_time > quick_max_time:
			quick_max_time = quick_time
	# Loop over the test sizes and sorting algorithms
	for algo in sorting_algos:
		if algo == 'Bubble':
			df.at[algo, size] = "Min {:.5f}, Max {:.5f}".format(bubble_min_time,bubble_max_time)
		elif algo == 'Insertion':
			df.at[algo, size] = "Min {:.5f}, Max {:.5f}".format(insertion_min_time,insertion_max_time)
		elif algo == 'Merge':
			df.at[algo, size] = "Min {:.5f}, Max {:.5f}".format(merge_min_time,merge_max_time)
		elif algo == 'Quick':
			df.at[algo, size] = "Min {:.5f}, Max {:.5f}".format(quick_min_time,quick_max_time)

# Print the DataFrame
print(df)

# Plot the dataframe as a table
fig, ax = plt.subplots()
ax.axis('off')
ax.axis('tight')
ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center')

# Save the figure as a PNG file
plt.savefig('already_sorted_arr.png', dpi=300)

print("Total time run: " + str(time.time() - very_start_time) + "s")

print("Done!")