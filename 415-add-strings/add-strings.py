class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        ans = ""

        while i >= 0 or j >= 0 or carry:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>= 0 else 0
            total = n1 + n2 + carry
            ans = str(total % 10) + ans
            carry = total // 10
            i -= 1
            j -= 1
        return ans


        