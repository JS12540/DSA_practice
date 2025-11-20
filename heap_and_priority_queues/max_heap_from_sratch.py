class MaxHeap:
    def __init__(self):
        # Internal array to store heap elements
        self.heap = []

    # -------- index helpers --------
    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # -------- heapify up (for insert) --------
    def _heapify_up(self, i):
        while i > 0:
            p = self._parent(i)
            # For MAX heap: child should NOT be greater than parent
            if self.heap[i] > self.heap[p]:
                self._swap(i, p)
                i = p
            else:
                break

    # -------- heapify down (for remove) --------
    def _heapify_down(self, i):
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            largest = i

            # choose the largest among node and its children
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            # if largest is not current index, swap and continue
            if largest != i:
                self._swap(i, largest)
                i = largest
            else:
                break

    # -------- public APIs --------
    def push(self, val):
        """Insert value into max heap. O(log n)"""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """Remove and return max element. O(log n)"""
        if not self.heap:
            raise IndexError("pop from empty heap")

        n = len(self.heap)
        self._swap(0, n - 1)
        max_val = self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        return max_val

    def peek(self):
        """Return max element without removing. O(1)"""
        if not self.heap:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __repr__(self):
        return f"MaxHeap({self.heap})"


if __name__ == "__main__":
    h = MaxHeap()

    for x in [3, 1, 6, 5, 2, 4]:
        h.push(x)
        print("After inserting", x, "->", h.heap)

    print("Max element (peek):", h.peek())

    print("\nPopping all elements:")
    while not h.is_empty():
        print(h.pop(), "   heap now:", h.heap)
