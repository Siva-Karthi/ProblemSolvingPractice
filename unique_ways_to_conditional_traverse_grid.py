"""
https://leetcode.com/problems/unique-paths/


A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.(ToDo : what does it mean )

"""

# def number_of_ways_to_destination(m: int, n: int) -> int:
#     if (m == 1 or n== 1):
#         return 1
#     else:
#         return number_of_ways_to_destination(m,n-1) +  number_of_ways_to_destination(m -1 ,n)

# if __name__ == '__main__':
#     print("number_of_ways_to_destination(3,7) is ", number_of_ways_to_destination(3,7))

"""
Dynamic programming?
   * Algorithm Design 
   * usage
        * combinations -?
        * optimaztion -?
   * 2 main conditions that problem should satisfy , so that we can use dynamic programming method
        * overlapping subproblem - done
        * optimal substructure
"""
# 10 * 5
# 5 * 10

# 5 * 2 

# total 15 amount = 100

# 100

# balance
# 50

# 0,1,1,2,3,5,8,13,21,34,

def fib(term):
   if term <= 1:
       return (term)
   else:
       return (fib(term-1) + fib(term-2)) # subproblem

def fib_using_dp(times=5):
    # 1.what is the objective function
    # 2.identify base cases
    # 3.write down the recurrence relation
    # 4.order of exec
    # 5.where to find answers
    fib_series = [ None for i in range(times+1)]
    fib_series[0] = 0
    fib_series[1] = 1
    fib_series[2] = 1
    for n in range(3, times+1): # [3,4,5]
        # print("n",n)
        fib_series[n] = fib_series[n-1] + fib_series[n-2]
    print("fib_series",fib_series)

def stair_case_problem(n=4):
    # 1.what is the objective function f(n)= number ways to to reach top of n steps by
    #                                        hopping 1 or 2 steps at a time
    # 2.identify base cases
    #     when n == 1, ans = 1
    # 3.write down the recurrence relation
    #     stair_case_problem(n) = stair_case_problem(n-1) +  stair_case_problem(n-2) 
    # 4.order of exec
    # 5.where to find answers
    if n< 1:
       return 0
    if n == 1:
        return 1
    else:
        return stair_case_problem(n-1) +  stair_case_problem(n-2) +  stair_case_problem(n-3) 
    
    
if __name__ == '__main__':
    # Change this value to adjust the number of terms in the sequence.
    # number_of_terms = 5
    # for i in range(number_of_terms):
    #     print(fib(i))
    print("stair_case_problem(10)",stair_case_problem(10))


# - - - - 
# 1 2 3 4

# 1 X 4  - 1 way

# 2 X 1, 1 X 1  - 2 nd way
# 3 X1  - 3rd way
# 1 X1 , 2X1 - 4th way
=======
def number_of_ways_to_destination(m: int, n: int) -> int:
    if (m == 1 or n== 1):
        return 1
    else:
        return number_of_ways_to_destination(m,n-1) +  number_of_ways_to_destination(m -1 ,n)

if __name__ == '__main__':
    print("number_of_ways_to_destination(3,7) is ", number_of_ways_to_destination(3,7))
