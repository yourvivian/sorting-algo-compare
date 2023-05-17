import random
import time
import matplotlib.pyplot as plt
import sys
import copy
sys.setrecursionlimit(10001)
import sorting_algo

very_start_time = time.time()

# Define max_size of arr, # of iterations, and max_value of each arr
max_size = 1000
max_value = 10000
num_iterations = 10

# Initialize empty lists to store average execution times
bubble_sort_times = []
insertion_sort_times = []
merge_sort_times = []
quick_sort_times = []
array_sizes = [i*10 for i in range(1,max_size//10)]

# Measure average execution times for different array sizes
for size in array_sizes:
	bubble_sort_avg_time = 0
	insertion_sort_avg_time = 0
	merge_sort_avg_time = 0
	quick_sort_avg_time = 0
    
	for i in range(num_iterations):
		random_array = [random.randint(1, max_value) for i in range(size)]
	
		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.bubble_sort(random_array_copy)
		bubble_sort_time = time.time() - start_time
		bubble_sort_avg_time += bubble_sort_time

		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.insertion_sort(random_array_copy)
		insertion_sort_time = time.time() - start_time
		insertion_sort_avg_time += insertion_sort_time

		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.merge_sort(random_array_copy)
		merge_sort_time = time.time() - start_time
		merge_sort_avg_time += merge_sort_time

		random_array_copy = copy.deepcopy(random_array)

		start_time = time.time()
		sorting_algo.quick_sort(random_array_copy, 0, size - 1)
		quick_sort_time = time.time() - start_time
		quick_sort_avg_time += quick_sort_time
    
	bubble_sort_avg_time /= num_iterations
	insertion_sort_avg_time /= num_iterations
	merge_sort_avg_time /= num_iterations
	quick_sort_avg_time /= num_iterations

	bubble_sort_times.append(bubble_sort_avg_time)
	insertion_sort_times.append(insertion_sort_avg_time)
	merge_sort_times.append(merge_sort_avg_time)
	quick_sort_times.append(quick_sort_avg_time)

# Create line graph
plt.plot(array_sizes, bubble_sort_times, label='Bubble Sort')
plt.plot(array_sizes, insertion_sort_times, label='Insertion Sort')
plt.plot(array_sizes, merge_sort_times, label='Merge Sort')
plt.plot(array_sizes, quick_sort_times, label='Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Average Execution Time (Seconds)')
plt.title('Sorting Algorithm Comparison (Unsorted Arr)\nMax Size={}, Max Value={}, Iterations={}'.format(max_size, max_value, num_iterations))
plt.text(0.2, 0.5, "Total time run: " + str(time.time() - very_start_time) + "s", fontsize=10, transform=plt.gcf().transFigure)
plt.legend()
plt.show()

print("Done!")
