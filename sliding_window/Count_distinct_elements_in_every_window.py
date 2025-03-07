## My solution


class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        l = []
        for i in range(n-k+1):
            count=0
            s = set()
            for j in range(i,i+k):
                s.add(arr[j])
            l.append(len(s))
            
        return l


import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

### Gfg soltuion

# Python program to count distinct elements in every window
# of size k by traversing all windows of size k

from collections import defaultdict

# Function to count distinct elements in every window of size k
def countDistinct(arr, k):
    n = len(arr)  
    res = []
    freq = defaultdict(int)
  
    # Store the frequency of elements of the first window
    for i in range(k):
        freq[arr[i]] += 1
  
    # Store the count of distinct elements of the first window
    res.append(len(freq))
  
    for i in range(k, n):
        freq[arr[i]] += 1
        freq[arr[i - k]] -= 1
      
        # If the frequency of arr[i - k] becomes 0, remove it from the hash map
        if freq[arr[i - k]] == 0:
            del freq[arr[i - k]]
      
        res.append(len(freq))
      
    return res


if __name__=='__main__':
      arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4

    res = countDistinct(arr, k)
    print(*res)
