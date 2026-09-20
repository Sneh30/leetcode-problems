# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n + 1):
            ans = ans ^ i

        for num in nums:
            ans = ans ^ num

        return ans
