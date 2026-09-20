class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i, ch in enumerate(s, 1):
            value = ord('z') - ord(ch) + 1
            ans += value * i

        return ans
        """
        :type s: str
        :rtype: int
        """
        