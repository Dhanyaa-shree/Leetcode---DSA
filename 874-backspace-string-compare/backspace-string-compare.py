class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            res = []

            for ch in string:
                if ch != "#":
                    res.append(ch)
                else:
                    if res:
                        res.pop()

            return "".join(res)

        return build(s) == build(t)
        