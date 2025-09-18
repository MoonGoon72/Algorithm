# https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for col in range(m + 1):
            dp[0][col] = col
        for row in range(n + 1):
            dp[row][0] = row
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    subsitutionCost = 0
                else:
                    subsitutionCost = 1
                dp[i][j] = min(dp[i-1][j-1] + subsitutionCost, dp[i-1][j] + 1, dp[i][j-1] + 1)
        
        return dp[n][m]
