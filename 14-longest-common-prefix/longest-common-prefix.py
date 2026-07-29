class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float("inf")
        i = 0
        for ch in strs:
            if len(ch) < min_len:
                min_len = len(ch)
        while i < min_len:
            for ch in strs:
                if ch[i] != strs[0][i]:
                    return ch[:i]
            i+=1
        return strs[0][:i]


        