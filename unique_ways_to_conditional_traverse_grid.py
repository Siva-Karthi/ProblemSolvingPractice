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

def number_of_ways_to_destination(m: int, n: int) -> int:
    if (m == 1 or n== 1):
        return 1
    else:
        return number_of_ways_to_destination(m,n-1) +  number_of_ways_to_destination(m -1 ,n)

if __name__ == '__main__':
    print("number_of_ways_to_destination(3,7) is ", number_of_ways_to_destination(3,7))