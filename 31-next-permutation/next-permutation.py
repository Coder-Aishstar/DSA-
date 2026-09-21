class Solution:
    def nextPermutation(self, nums):
        i = len(nums) - 2

        # Find the first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Find element just greater than nums[i]
        if i >= 0:
            j = len(nums) - 1

            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the elements after i
        nums[i + 1:] = reversed(nums[i + 1:])
       