class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for a, b in zip(s, t):
            if a in d:
                if d[a] != b:
                    return False
            else:
                d[a] = b
        return len(set(d.values())) == len(d)
        