class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n+1)
        dp[1] = 1
        
        share = 0 
        for i in range(2, n+1):
            if i - delay >= 1: 
                share = (share + dp[i - delay]) % mod

            if i - forget >= 1: 
                share = (share - dp[i-forget] + mod) % mod 
            dp[i] = share 

        start = max(1,n - forget + 1)
        total = 0 
        for i in range(start, n+1): 
            total = (total + dp[i]) % mod
        
        return total