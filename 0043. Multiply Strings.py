class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                sum_ = mul + res[i + j + 1]
                res[i + j + 1] = sum_ % 10
                res[i + j] += sum_ // 10
        return ''.join(map(str, res)).lstrip('0')
