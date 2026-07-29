class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        seen = set()

        for ch in s:
            if ch in seen:
                count += 2
                seen.remove(ch)
            else:
                seen.add(ch)
        if seen:
            return count + 1
        else:
            return count
        