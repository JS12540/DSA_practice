# Python Program to check for triplet sum using Sorting
# and Two Pointer Technique

def hasTripletSum(arr, target):
    n = len(arr)
    arr.sort()
    
    # Fix the first element as arr[i]
    for i in range(n - 2):
        
        # Initialize left and right pointers with 
        # start and end of remaining subarray
        l = i + 1
        r = n - 1
        
        requiredSum = target - arr[i]
        while l < r:
            if arr[l] + arr[r] == requiredSum:
                return True
            if arr[l] + arr[r] < requiredSum:
                l += 1
            else:
                r -= 1
    
    # If we reach here, then no triplet was found
    return False

if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    target = 13
    if hasTripletSum(arr, target):
        print("true")
    else:
        print("false")
