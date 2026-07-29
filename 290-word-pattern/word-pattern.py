class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()

        if len(pattern) != len(word):
            return False 
        
        d = {}
        for a, b in zip(pattern, word):
            if a in d:
                if d[a] != b:
                    return False
            else:
                d[a] = b
        return len(set(d.values())) == len(d) 
        