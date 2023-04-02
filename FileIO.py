import Board

class FileIO:
    def __init__(self, layout):
        self.data = []
        self.f = open(layout)
        self.file = self.f.read

        for line in self.file:
            row = []
            for ch in line:
                row.append(int(ch))
            self.data.append(row)
        
        for r in self.data:
            for c in self.data[r]:
                count = 0
                if(self.data[r][c] == 0):
                    neighbors = [(r - 1, c - 1), (r - 1, c   ), (r - 1, c + 1),
                                (r    , c - 1),                (r    , c + 1),
                                (r + 1, c - 1), (r + 1, c   ), (r + 1, c + 1),]
                    for i in neighbors:
                        if(isValid(self.data, i[0], i[1])):
                            if(self.data[i[0]][i[1]] == 9):
                                count += 1
                    self.data[r][c] == count
            

        def isValid(plane, r, c):
            if(r >= 0 & r < len(plane)):
                if(c >= 0 & c < len(plane[r])):
                    return True
            else:
                return False


        self.b = Board(self.data)
        self.f.close()
    
    def getBoard(self):
        return self.b
    
if __name__ == "main":
    test = FileIO("testFile.txt")
    board = test.getBoard()

    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print()
