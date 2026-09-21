class Solution:
    def resultArray(self, nums, k):
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            num %= k

            # Subarray containing only this number
            new_dp[num] = 1

            # Extend previous subarrays
            for r in range(k):
                new_r = (r * num) % k
                new_dp[new_r] += dp[r]

            # Add all subarrays ending here to answer
            for r in range(k):
                ans[r] += new_dp[r]

            dp = new_dp

        return ans