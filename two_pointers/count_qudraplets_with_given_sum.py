from collections import defaultdict


class Solution:

    def countSum(self, arr, target):
        count = 0
        n = len(arr)
        # Store the frequency of sum of first two elements
        m = defaultdict(int)

        # Traverse from 0 to n-1, where arr[i] is the 3rd element
        for i in range(n - 1):
            # All possible 4th elements
            for j in range(i + 1, n):
                temp = arr[i] + arr[j]
                count += m[target - temp]

            # Store frequency of all possible sums of first two elements
            for j in range(i):
                temp = arr[i] + arr[j]
                m[temp] += 1

        return count

# Driver code
arr = [1, 1, 1, 1, 1]
target = 4
