'''
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find number of distinct combinations to reach the given score.

Input
n = 10
Output
2
Explanation
There are two ways {5,5} and {10}.

'''

def count(n: int) -> int:
        table = [0] * (n + 1)
        table[0] = 1  # If 0 sum is required, the number of ways is 1.
        
        for i in range(3, n + 1):
            table[i] += table[i - 3]  # For every point (3, 5, 10), add the number of ways to reach that sum before adding these points.
        for i in range(5, n + 1):
            table[i] += table[i - 5]
        for i in range(10, n + 1):
            table[i] += table[i - 10]
        print(table)
        return table[n]
        

# Test the function
n = 20
print("Number of distinct combinations:", count(n))


