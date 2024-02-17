list = [0, 1]

def dep_fibonnaci(n):
    # Base case: if the Fibonacci number is already computed, return it directly
    if n < len(list):
        return list[n]
    else:
        # Recurrence relation: F(n) = F(n-1) + F(n-2)
        # Define state: Implicitly handled through function arguments and memoization list
        value = dep_fibonnaci(n-1) + dep_fibonnaci(n-2)
        # Memoization: Store the computed Fibonacci number to avoid redundant calculations
        list.append(value)
        return value
    
print("Initial Fibonacci list:", list)

# Test cases
print("Fibonacci number at index 3:", dep_fibonnaci(3))
print("Updated Fibonacci list after computing Fibonacci number at index 3:", list)

print("Fibonacci number at index 5:", dep_fibonnaci(5))
print("Updated Fibonacci list after computing Fibonacci number at index 5:", list)
