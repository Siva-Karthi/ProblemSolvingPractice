"""
maximum weight of plates for the barbell within maxCapacity
"""

weights = [7, 1, 5, 6, 2]
maxCapacity = 7
# max sub array sum less than - maxCapacity


"""
(   [1, 4, 3, 5], 7, 7),  # Best combo 4 + 3
    [1, 5,  ]
    
                         1
    4                5       1
    
    
                         1                    4
                    5       1              7    4  
    
    3            5     5     
                
    
max( )

([1, 2, 3], 6, 6),  # All weights can be used
([], 5, 0),  # No weights
([5], 5, 5),  # Single weight equals capacity
([6, 4, 3], 5, 4),  # Cannot combine to make 5
([8, 10, 9], 7, 0),  # All weights too large
([1, 1, 1, 1, 1, 1, 1], 5, 5),  # Duplicates
([1, 4, 3, 5], 7, 7),  # Best combo 4 + 3
"""

"""
dp = [0] * (maxCapacity + 1)
for w in weights:
    for j in range(maxCapacity, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + w)
return dp[maxCapacity]
"""
