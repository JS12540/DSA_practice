### Dynamic Programming Problem Solving Steps

- Typically, all the problems that require maximizing or minimizing certain quantities or counting problems that say to count the arrangements under certain conditions or certain probability problems can be solved by using Dynamic Programming.
- All dynamic programming problems satisfy the overlapping subproblems property and most of the classic Dynamic programming problems also satisfy the optimal substructure property. Once we observe these properties in a given problem be sure that it can be solved using Dynamic Programming.

1. **Understand the Problem**:
   - Read and analyze the problem statement carefully.
   - Identify the input, output, constraints, and requirements.

2. **Identify Optimal Substructure**:
   - Determine if the problem can be broken down into smaller subproblems.Essentially, a subproblem is a smaller version of the main problem that you're trying to solve. In dynamic programming, you solve these smaller subproblems and then use their solutions to build up       to the solution of the main problem.
   - Once we've identified the subproblems, we need to establish a relationship between the main problem and its subproblems. This relationship is called a recurrence relation. It describes how we can use solutions to smaller subproblems to solve the main problem.
   - Verify if the optimal solution to the problem depends on the optimal solutions to its subproblems.

3. **Overlapping Subproblems**:
   - Determine if the same subproblems are solved multiple times in the process of solving the larger problem.
   - Dynamic programming optimizes efficiency by solving each subproblem only once and storing the solution for future reference, avoiding redundant computations.

4. **Define State**:
   - Identify the parameters or variables that define the state of the problem.
   - States represent the different configurations or situations encountered while solving the problem.

5. **Formulate Recurrence Relation**:
   - Express the problem in terms of a recurrence relation.
   - Define how the solution to a larger problem can be computed from the solutions to its subproblems.

6. **Determine Base Cases**:
   - Identify the smallest subproblems or base cases that can be solved directly.
   - Base cases serve as the starting point for solving larger subproblems.

7. **Choose a DP Strategy**:
   - Decide whether to use a bottom-up or top-down approach based on the problem's characteristics and constraints.
   - Bottom-up: Solve smaller subproblems first and build up to solve larger subproblems iteratively.
   - Top-down (Memoization): Start with the original problem and recursively solve subproblems, caching results to avoid redundant computations.

8. **Implement the Algorithm**:
   - Write code to implement the dynamic programming solution based on the chosen strategy.
   - Ensure that the recurrence relation and base cases are correctly implemented.

9. **Optimize Space and Time Complexity**:
   - Optimize the solution to reduce space and time complexity.
   - Look for opportunities to minimize memory usage and improve runtime performance.

10. **Test and Debug**:
    - Test the solution with different inputs, including edge cases and boundary conditions.
    - Debug any errors or issues encountered during testing.

11. **Optimize Further (if needed)**:
    - Identify any bottlenecks or areas for improvement in the solution.
    - Optimize the algorithm further to achieve better performance if necessary.


|                     | Tabulation                                    | Memoization                                   |
|---------------------|-----------------------------------------------|-----------------------------------------------|
| State               | State transition relation is difficult to think | State transition relation is easy to think   |
| Code                | Code gets complicated when a lot of conditions are required | Code is easy and less complicated           |
| Speed               | Fast, as we directly access previous states from the table | Slow due to a lot of recursive calls and return statements |
| Subproblem solving | If all subproblems must be solved at least once, a bottom-up dynamic programming algorithm usually outperforms a top-down memoized algorithm by a constant factor | If some subproblems in the subproblem space need not be solved at all, the memoized solution has the advantage of solving only those subproblems that are definitely required |
| Table entries       | In the Tabulated version, starting from the first entry, all entries are filled one by one | Unlike the Tabulated version, all entries of the lookup table are not necessarily filled in Memoized version. The table is filled on demand. |
| Approach            | Generally, tabulation(dynamic programming) is an iterative approach | On the other hand, memoization is a recursive approach. |
