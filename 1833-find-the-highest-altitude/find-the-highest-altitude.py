class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        max_alt = 0
        for i in gain:
            curr += i
            if curr > max_alt:
                max_alt = curr
        return max_alt
        