"""
MinHeap and MaxHeap using Python's heapq library.
Both implemented in a single file.
"""

import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        """Insert value into min-heap"""
        heapq.heappush(self.heap, val)

    def pop(self):
        """Remove and return smallest value"""
        if not self.heap:
            raise IndexError("pop from empty MinHeap")
        return heapq.heappop(self.heap)

    def peek(self):
        """Return smallest value without removing"""
        if not self.heap:
            raise IndexError("peek from empty MinHeap")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __repr__(self):
        return f"MinHeap({self.heap})"


class MaxHeap:
    def __init__(self):
        # We will store NEGATIVE values internally,
        # because heapq is a min-heap.
        self.heap = []

    def push(self, val):
        """Insert value into max-heap"""
        # push negative so the largest becomes smallest (in negative)
        heapq.heappush(self.heap, -val)

    def pop(self):
        """Remove and return largest value"""
        if not self.heap:
            raise IndexError("pop from empty MaxHeap")
        # pop negative and return positive
        return -heapq.heappop(self.heap)

    def peek(self):
        """Return largest value without removing"""
        if not self.heap:
            raise IndexError("peek from empty MaxHeap")
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __repr__(self):
        # show as positive values for readability
        return "MaxHeap([" + ", ".join(str(-x) for x in self.heap) + "])"


# ------------------ Demo / Example usage ------------------
if __name__ == "__main__":
    print("=== MinHeap Demo ===")
    minh = MinHeap()
    for x in [5, 3, 8, 1, 2]:
        print(f"Pushing {x} into MinHeap")
        minh.push(x)
        print("Current MinHeap:", minh)

    print("Peek min:", minh.peek())
    while not minh.is_empty():
        print("Pop:", minh.pop(), "   Heap now:", minh)

    print("\n=== MaxHeap Demo ===")
    maxh = MaxHeap()
    for x in [5, 3, 8, 1, 2]:
        print(f"Pushing {x} into MaxHeap")
        maxh.push(x)
        print("Current MaxHeap:", maxh)

    print("Peek max:", maxh.peek())
    while not maxh.is_empty():
        print("Pop:", maxh.pop(), "   Heap now:", maxh)
