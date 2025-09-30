class Solution:
    def partitionString(self, s: str) -> List[str]:
        result = []
        curr_sub = ""
        seen = set()

        for i in range(len(s)):
            ch = s[i]
            curr_sub = curr_sub + ch

            if curr_sub not in seen:
                seen.add(curr_sub)
                result.append(curr_sub)
                curr_sub = ""       
        return result
