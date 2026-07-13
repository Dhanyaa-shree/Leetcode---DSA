class Solution:
    def buildArray(self, nums):
        arr = []
        for i in range(len(nums)):
            ans = nums[nums[i]]
            arr.append(ans)
        return arr
