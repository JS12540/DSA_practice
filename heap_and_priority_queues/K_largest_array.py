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

import heapq

l=[3, 10, 6, 7, 2, 9]
k=3

heap = []
for x in l:
    if len(heap) < k:
        heapq.heappush(heap, x)
    else:
        if x>heap[0]:
            heapq.heapreplace(heap,x)
    print(heap)
    
print(heap)
