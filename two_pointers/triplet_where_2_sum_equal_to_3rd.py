# Function to find if there exists a triplet in the array

def find_triplet(arr):
    n = len(arr)
    
    # Sort the array
    arr.sort()

    # Iterate through the array
    for i in range(2, n):
        left, right = 0, i - 1
        
        while left < right:
            sum = arr[left] + arr[right]
            
            if sum == arr[i]:  
                return True
            elif sum < arr[i]:  
                left += 1
            else:  
                right -= 1
    
    return False

# Driver Code with Predefined Input
arr = [1, 2, 3, 4, 5]  

if find_triplet(arr):
    print("true")
else:
    print("false")
