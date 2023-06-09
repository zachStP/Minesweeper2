from Board import Board

class FileIO:
    def __init__(self, layout):
        def isValid(plane, r, c):
            if(r >= 0 and r < len(plane)):
                if(c >= 0 and c < len(plane[r])):
                    return True
                else:
                    return False
            else:
                return False
        
        
        self.data = []
        f = open(layout, 'r')

        for line in f:
            row = []
            for ch in line:
                if(ch != "\n"):
                    row.append(int(ch))
            self.data.append(row)
        
        for r in range(len(self.data)):
            for c in range(len(self.data[r])):
                count = 0
                if(self.data[r][c] != 9):
                    neighbors = [(r - 1, c - 1), (r - 1, c   ), (r - 1, c + 1),
                                (r    , c - 1),                (r    , c + 1),
                                (r + 1, c - 1), (r + 1, c   ), (r + 1, c + 1)]
                    for i in neighbors:
                        if(isValid(self.data, i[0], i[1])):
                            if(self.data[i[0]][i[1]] == 9):
                                count += 1
                    self.data[r][c] = count
        self.b = Board(self.data)
        f.close()
    
    def getBoard(self):
        return self.b
    
if __name__ == "__main__":
    test = FileIO("testFile.txt")
    board = test.getBoard()

    for i in range(len(board.data)):
        for j in range(len(board.data[i])):
            print(board.data[i][j], end="")
        print()
