l = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maximum_subarray_sum(l):
    if len(l) == 0:
        print("Array is empty")
        return 0
    elif len(l) == 1:
        print("Array contains only one element")
        return l[0]
    else:
        maximum = current = l[0]
        for i in range(1, len(l)):
            if l[i] > current + l[i]:
                current = l[i]
            else:
                current += l[i]
            
            if current > maximum:
                maximum = current
            print(f"At index {i}, current sum: {current}, maximum sum: {maximum}")
        return maximum
    
sum = maximum_subarray_sum(l)
print(sum)