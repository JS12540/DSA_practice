class MinHeap():
    def __init__(self):
        self.heap=[]
        
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2
        
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def _heapify_up(self, i):
        while i > 0:
            p = self._parent(i)
            # If current is smaller than parent, swap
            if self.heap[i] < self.heap[p]:
                self._swap(i, p)
                i = p
            else:
                break
            
    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            # Check left child
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check right child
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            # If smallest is not the current index, swap and continue
            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break
    
    def push(self, val):
        """
        Insert a new value into the heap.
        Time: O(log n)
        """
        self.heap.append(val)          # Add at the end
        self._heapify_up(len(self.heap) - 1)
            
    def pop(self):
        """
        Remove and return the minimum element.
        Time: O(log n)
        Raises IndexError if heap is empty.
        """
        if not self.heap:
            raise IndexError("pop from empty heap")

        n = len(self.heap)
        # Swap root with last element
        self._swap(0, n - 1)
        min_val = self.heap.pop()      # Remove last (old root)

        # Heapify down from root if not empty
        if self.heap:
            self._heapify_down(0)

        return min_val
    
    def peek(self):
        """
        Return the minimum element without removing it.
        Time: O(1)
        """
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __len__(self):
        """
        Return number of elements in heap.
        """
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __repr__(self):
        return f"MinHeap({self.heap})"
        
    
if __name__ == "__main__":
    h = MinHeap()

    # Insert elements
    h.push(5)
    h.push(2)
    h.push(8)
    h.push(1)
    h.push(10)

    print("Heap:", h)          # Internal heap array

    print("Min element:", h.peek())  # Should be 1

    while not h.is_empty():
        print("Popped:", h.pop())
