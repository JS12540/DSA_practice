## My solution

class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        n = len(arr)
        max_array = []
        i = 0
        j = k-1
        while(j<n):
            subarray = arr[i:j+1]
            max_array.append(max(subarray))
            i+=1
            j+=1
        return max_array

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")



### More Good solution which I have not implemented

from collections import deque

# Method to find the maximum for each
# and every contiguous subarray of size k.
def maxOfSubarrays(arr, k):
    n = len(arr)

    # to store the results
    res = []
  
    # create deque to store max values
    dq = deque()

    # Process first k (or first window) elements of array
    for i in range(0, k):
      
        # For every element, the previous smaller elements 
        # are useless so remove them from dq
        while dq and arr[i] >= arr[dq[-1]]:
          
            # Remove from rear
            dq.pop()

        # Add new element at rear of queue
        dq.append(i)

    # Process rest of the elements, i.e., from arr[k] to arr[n-1]
    for i in range(k, len(arr)):
      
        # The element at the front of the queue is the largest 
        # element of previous window, so store it
        res.append(arr[dq[0]])

        # Remove the elements which are out of this window
        while dq and dq[0] <= i - k:
          
            # Remove from front of queue
            dq.popleft()

        # Remove all elements smaller than the currently being 
        # added element (remove useless elements)
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()

        # Add current element at the rear of dq
        dq.append(i)

    # store the maximum element of last window
    res.append(arr[dq[0]])

    return res

if __name__ == "__main__":
    arr = [1, 3, 2, 1, 7, 3]
    k = 3
    res = maxOfSubarrays(arr, k)
    for maxVal in res:
        print(maxVal, end=" ")
