class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # given mxn grid  characters board and return True if the word exist

        dxn = [[0,1],[1,0],[-1,0],[0,-1]]
        # first look for the first letter
        letter = []
        first_letter = word[0]
        n = len(board)
        m = len(board[0])
        x = len(word)
        visited = set()

        # a tracks the position of the letter in the word
        def track(i,j, a):
            if a==x:
                return True
            if (i, j) in visited or board[i][j] != word[a]:
                return False
            # handle...1 letter
            if x==1:
                return True

            visited.add((i, j))
            for c, d in dxn:
                nxt_row, nxt_col = i + c, j + d
                if 0 <= nxt_row < n and 0 <= nxt_col < m:
                    if track(nxt_row, nxt_col, a + 1):
                        return True
            
            # to handle [["C","A","A"],["A","A","A"],["B","C","D"]]
            visited.remove((i,j))
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j]==first_letter:
                    if  track(i,j, 0):
                        return True
        
        return False


