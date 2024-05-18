"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""

"""
intuition: the number of ways to make up a some with some number of coins is the sum of ways to make the number without last coin and number of ways adding the last coin would create.
the number of ways adding the new coin would create is the number of ways the amount - last coin would have without the coin as we can add the last coin to all of them.
"""

def count(coins, n, target_sum):
    # 2D dp array where n is the number of coin denominations and target_sum is the target sum
    dp = [[0 for j in range(target_sum + 1)] for i in range(n + 1)]
 
    # Represents the base case where the target sum is 0, and there is only one way to make change: by not selecting any coin
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            # Add the number of ways to make change without using the current coin
            dp[i][j] += dp[i - 1][j]
 
            if j - coins[i - 1] >= 0:
                # Add the number of ways to make change using the current coin
                dp[i][j] += dp[i][j - coins[i - 1]]
 
    return dp[n][target_sum]
