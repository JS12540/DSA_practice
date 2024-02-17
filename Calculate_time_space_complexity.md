# Calculating Time Complexity:

## 1. Identify Operations:
Identify the basic operations in your code that contribute to its running time. Common operations include arithmetic operations, comparisons, assignments, and function calls.

## 2. Count Operations:
Determine how many times each basic operation is executed as a function of the input size. This often involves analyzing loops, recursive calls, and other control flow structures.

## 3. Determine Dominant Terms:
Identify the most significant terms in the total count of operations. Ignore constant factors and lower-order terms, focusing on the term(s) that grow fastest with the input size.

## 4. Express Complexity:
Express the time complexity using Big O notation, focusing on the dominant terms identified in the previous step. For example, O(n), O(n^2), O(log n), etc.

# Calculating Space Complexity:

## 1. Identify Variables:
Identify the variables and data structures used in your code that consume memory. This includes primitive data types, arrays, objects, and dynamically allocated memory.

## 2. Track Memory Usage:
Determine how much memory each variable and data structure consumes as a function of the input size. Account for any additional memory required for function calls, recursion, and other runtime activities.

## 3. Determine Dominant Terms:
Identify the most significant terms in the total memory usage. Similar to time complexity analysis, focus on the terms that grow fastest with the input size and ignore constant factors and lower-order terms.

## 4. Express Complexity:
Express the space complexity using Big O notation, emphasizing the dominant terms identified in the previous step. For example, O(n), O(n^2), O(log n), etc.

By following these steps, you can systematically analyze the time and space complexity of any code, helping you understand its performance characteristics and scalability.
