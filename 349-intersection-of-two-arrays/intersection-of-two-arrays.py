class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        result =[]

        for ch in nums2:
            if ch in nums1 and ch not in result:
                result.append(ch)
        return result
        