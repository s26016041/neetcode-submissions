class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for l in board:
            if self.ifRepeat(l):
                return False

        for i in range(9):
            if self.ifRepeat([row[i] for row in board]):
                return False

        for i in range(1, 9, 3):
            for j in range(1, 9, 3):
                box = []
                for r in [i-1, i, i+1]:     
                    for c in [j-1, j, j+1]:  
                        box.append(board[r][c])
                
                if self.ifRepeat(box):
                    return False

        return True
        
    def ifRepeat(self, board: List[str]) -> bool:
        boardDict={}

        for number in board:
            if number == ".":
                continue

            if number in boardDict:
                return True
                
            boardDict[number] = True
        
        return False