class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # neetcode

        # track the opening and the closing of the parentheses
        # if open==close==n: return it
        # if open<n: opening parenthesis could be added
        # if close<open: closing parenthesis could be added

        res = []
        def backtrack(ans, open, close):
            if open==close==n:
                res.append(ans)
                return

            if open<n:
                backtrack(ans + "(", open+1,close)
            
            if close<open:
                backtrack(ans + ")", open, close+1)

        backtrack("", 0, 0)

        return res
