class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        n, m = len(word1), len(word2)
        res = ""

        while ptr1 < n or ptr2 < m:
            if ptr1 == n:
                res += word2[ptr2:]
                break
            if ptr2 == m:
                res += word1[ptr1:]
                break

            a, b = word1[ptr1], word2[ptr2]


            if word1[ptr1:] > word2[ptr2:]:
                res += a
                ptr1 += 1
            else:
                res += b
                ptr2 += 1

        return res
