class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_streak = 0

        for n in numset:
            if (n-1) not in numset:
                curr_streak = 1 
        
                while (n+curr_streak) in numset:
                    curr_streak += 1 
        
                longest_streak = max(curr_streak, longest_streak)
        return longest_streak

        