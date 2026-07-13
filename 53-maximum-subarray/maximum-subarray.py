class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = 0
        for i in nums:
            if current < 0:
                current = 0
            current += i
            if current > max_sum:
                max_sum = current 
        return max_sum
        