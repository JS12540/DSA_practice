class Solution:
    def maximumSumSubarray (self,arr,k):
        n = len(arr)
        window_sum = sum(arr[:k])
        maximum = window_sum
        
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]  # Add new element, remove old element
            maximum = max(maximum, window_sum)
        
        return maximum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.maximumSumSubarray(arr, k)
        print(ans)
        tc -= 1
        print("~")
