# ==========================================
# Q1. Implement a Min-Heap using a list
# ------------------------------------------
# Write a class MinHeap that supports:
# - insert(val)
# - extract_min()
# - get_min()
#
# Example:
# Input:
#   h = MinHeap()
#   h.insert(5)
#   h.insert(2)
#   h.insert(8)
#   print(h.extract_min())
#
# Output:
#   2
#
# Time Complexity:
#   insert(val):      O(log N)
#   extract_min():    O(log N)
#   get_min():        O(1)
# Space Complexity:
#   O(N)  to store all elements in the heap
# ==========================================



# ==========================================
# Q2. K largest elements from an array
# ------------------------------------------
# Using a Min-Heap, find the K largest
# numbers in an array.
#
# Example:
# Input:
#   arr = [3, 10, 6, 7, 2, 9]
#   k = 3
#
# Output:
#   [7, 9, 10]
#
# Time Complexity:
#   O(N log K)
#   (Each of N elements may do a push/pop on heap of size K)
# Space Complexity:
#   O(K)  for the min-heap
# ==========================================



# ==========================================
# Q3. Merge K Sorted Lists using Min-Heap
# ------------------------------------------
# Each list is sorted. Merge them into
# one sorted list using a priority queue.
#
# Example:
# Input:
#   lists = [
#       [1,4,5],
#       [1,3,4],
#       [2,6]
#   ]
#
# Output:
#   [1,1,2,3,4,4,5,6]
#
# Let K = number of lists,  N = total number of elements.
#
# Time Complexity:
#   O(N log K)
#   (Each of N elements is pushed/popped in heap of size K)
# Space Complexity:
#   O(K) for the heap
#   O(N) for the output list
# ==========================================



# ==========================================
# Q4. Find the Kth smallest element
# ------------------------------------------
# Use a Max-Heap of size K to find the
# K-th smallest element.
#
# Example:
# Input:
#   arr = [7, 10, 4, 3, 20, 15]
#   k = 3
#
# Output:
#   7
#   (The 3rd smallest element)
#
# Time Complexity:
#   O(N log K)
#   (Build / maintain a max-heap of size K over N elements)
# Space Complexity:
#   O(K)  for the max-heap
# ==========================================



# ==========================================
# Q5. Priority Queue task scheduler
# ------------------------------------------
# Given tasks with priorities, simulate
# scheduling using a Max-Heap.
#
# Example:
# Input:
#   tasks = [(3,"A"), (1,"B"), (5,"C")]
#
# Output:
#   Execution order:
#   C, A, B
#
# Let N = number of tasks.
#
# Time Complexity:
#   Building heap:    O(N)  (if heapified at once)
#   Or inserting:     O(N log N) (if pushed one by one)
#   Each pop:         O(log N)
#   Overall:          O(N log N) for scheduling all tasks
# Space Complexity:
#   O(N)  for storing tasks in the heap
# ==========================================



# ==========================================
# Q6. Find Median in a running stream
# ------------------------------------------
# Use two heaps:
# - Max-Heap for lower half
# - Min-Heap for upper half
#
# Example:
# Input stream:
#   [5, 15, 1, 3]
#
# Output medians:
#   5, 10, 5, 4
#
# Let N = number of elements in the stream.
#
# Time Complexity:
#   For each insertion:   O(log N)
#   Getting median:       O(1)
#   For full stream:      O(N log N)
# Space Complexity:
#   O(N)  (all numbers stored in two heaps)
# ==========================================



# ==========================================
# Q7. Reorganize String (No Adjacent Same)
# ------------------------------------------
# Use a Max-Heap to ensure highest freq
# characters are placed first.
#
# Example:
# Input:
#   s = "aab"
#
# Output:
#   "aba"
#
# Let N = length of string, U = number of unique chars.
#
# Time Complexity:
#   Counting frequencies:    O(N)
#   Building heap:           O(U)
#   Each pop/push operation: O(log U), repeated O(N) times
#   Overall:                 O(N log U)
# Space Complexity:
#   O(U)  for frequency map + heap
#   O(N)  for output string
# ==========================================



# ==========================================
# Q8. Top K frequent elements
# ------------------------------------------
# Use a Min-Heap of size K to return the
# most frequent elements.
#
# Example:
# Input:
#   arr = [1,1,1,2,2,3]
#   k = 2
#
# Output:
#   [1, 2]
#
# Let N = size of array, U = number of unique elements.
#
# Time Complexity:
#   Counting frequencies:   O(N)
#   Maintaining heap size K over U keys: O(U log K)
#   Overall:                O(N + U log K)
# Space Complexity:
#   O(U)  for frequency map
#   O(K)  for the heap
# ==========================================



# ==========================================
# Q9. Sort a nearly sorted array (K-sorted)
# ------------------------------------------
# Use a Min-Heap to sort an array where
# every element is at most K positions away.
#
# Example:
# Input:
#   arr = [6,5,3,2,8,10,9]
#   k = 3
#
# Output:
#   [2,3,5,6,8,9,10]
#
# Let N = size of array.
#
# Time Complexity:
#   O(N log K)
#   (Each of N elements is pushed/popped from heap of size at most K+1)
# Space Complexity:
#   O(K)  for the heap
# ==========================================



# ==========================================
# Q10. Connect N ropes with minimum cost
# ------------------------------------------
# Use a Min-Heap to repeatedly connect
# smallest ropes first.
#
# Example:
# Input:
#   ropes = [4,3,2,6]
#
# Output:
#   29
# Explanation:
#   (2+3)=5
#   (5+4)=9
#   (9+6)=15
#   Total = 29
#
# Let N = number of ropes.
#
# Time Complexity:
#   Building heap:      O(N)
#   Each combine step:  O(log N), done (N - 1) times
#   Overall:            O(N log N)
# Space Complexity:
#   O(N)  for the heap
# ==========================================
