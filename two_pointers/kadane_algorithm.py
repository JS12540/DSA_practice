class Solution:
    def maxSubArraySum(self, arr):
        # Your code here

        n = len(arr)
        res = arr[0]
        max_ending = arr[0]
        for i in range(1,n):
            max_ending = max(max_ending + arr[i],arr[i])
            res = max(res,max_ending)
        return res

import math
def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()
