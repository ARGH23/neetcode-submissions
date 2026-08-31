class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #rows
        for row in board:
            x = set()

            for num in row:
                if num != "." and num in x:
                    return False
                else:
                    x.add(num)

        #cols
        for i in range(9):
            x = set()

            for j in range(9):
                num = board[j][i]

                if num != "." and num in x:
                    return False
                else:
                    x.add(num)


        #boxes
        for i in range(3):
            

            for j in range(3):
                
                x = set()

                sx = i*3
                sy = j*3

                for k in range(9):
                    num = board[sx + int(k/3)][sy + k%3]

                    if num != "." and num in x:
                        return False
                    else:
                        x.add(num)
                


        return True