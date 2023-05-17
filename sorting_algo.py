# Implementation of Bubble Sort
def bubble_sort(arr):
	n = len(arr)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

# Implementation of Insertion Sort
def insertion_sort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1, len(arr)):

		key = arr[i]

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


# Implementation of merge_sort
def merge_sort(arr):
	if len(arr) > 1:

		# Finding the mid of the array
		mid = len(arr)//2

		# Dividing the array elements
		L = arr[:mid]

		# into 2 halves
		R = arr[mid:]

		# Sorting the first half
		merge_sort(L)

		# Sorting the second half
		merge_sort(R)

		i = j = k = 0

		# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

# Implementation of quick_sort

# Function to find the partition position
def partition(arr, low, high):

	# Choose the rightmost element as pivot
	pivot = arr[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if arr[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(arr[i], arr[j]) = (arr[j], arr[i])

	# Swap the pivot element with
	# e greater element specified by i
	(arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

	# Return the position from where partition is done
	return i + 1

# Implementation to perform quicksort

def quick_sort(arr, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(arr, low, high)

		# Recursive call on the left of pivot
		quick_sort(arr, low, pi - 1)

		# Recursive call on the right of pivot
		quick_sort(arr, pi + 1, high)