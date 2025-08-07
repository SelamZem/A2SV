class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # the 8 dxn
        dxn = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
        n, m = len(board), len(board[0])
        board2 = copy.deepcopy(board)

        for i in range(n):
            for j in range(m):
                num_of_ones = 0
                num = board2[i][j]
                for x, y in dxn:
                    newr, newc= i+x, j+y
                    if 0<=newr<n and 0<=newc<m:
                        if board2[newr][newc]==1:
                            num_of_ones +=1

                if num==1 and num_of_ones<2 or num==1 and num_of_ones>3:
                    board[i][j]=0
                elif  num==0 and num_of_ones==3:
                    board[i][j]=1
                else:
                    board[i][j]=num

                



        