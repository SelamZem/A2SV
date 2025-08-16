class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        res = ['x'] * n

        for i in range(n):
            a = indices[i]
            res[a] = s[i]


        return "".join(res)