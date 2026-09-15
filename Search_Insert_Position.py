# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lb=n
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid] >= target:
                lb=mid
                hi=mid-1
            else:
                lo=mid+1
        return lb
