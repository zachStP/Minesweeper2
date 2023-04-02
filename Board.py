
class Board:
    def __init__(self, data):
        if data is None:
            self.data = [[0 for j in range(16)] for i in range(16)]
            self.display = [[0 for j in range(16)] for i in range(16)]
            return
        else:
            self.data = [[data[i][j] for j in range(16)] for i in range(16)]
            self.display = [[False for j in range(16)] for i in range(16)]

    def isValid(self, plane, r, c):
        if(r >= 0 and r < len(plane)):
            if(c >= 0 and c < len(plane[r])):
                return True
            else:
                return False
        else:
            return False

    def isMine(self, plane, r, c):
        if(self.isValid(plane, r, c)):    
            if(plane[r][c] == 9 or plane[r][c] == -9):
                return True
        return False
    
    def countNeighborMines(self, r, c):
        count = 0
        if(self.data[r][c] != 9):
            neighbors = [(r - 1, c - 1), (r - 1, c   ), (r - 1, c + 1),
                        (r    , c - 1),                (r    , c + 1),
                        (r + 1, c - 1), (r + 1, c   ), (r + 1, c + 1)]
            for i in neighbors:
                if(self.isValid(self.data, i[0], i[1])):
                    if(self.data[i[0]][i[1]] == 9):
                        count += 1
                    self.data[r][c] = count

    def updateNeighbors(self, r, c):
        neighbors = [(r - 1, c - 1), (r - 1, c   ), (r - 1, c + 1),
                    (r    , c - 1),                (r    , c + 1),
                    (r + 1, c - 1), (r + 1, c   ), (r + 1, c + 1)]
        for i in neighbors:
            if(self.isValid(self.data, i[0], i[1])):
                self.countNeighborMines(i[0], i[1])

    def changeDataAtTo(self, r, c, value):
        self.data[r][c] = value
        self.updateNeighbors(r, c)

    def moveMineAtTo(self, currentR, currentC, newR, newC):
        if self.isValid(self.data, currentR, currentC) and self.isValid(self.data, newR, newC):
            self.data[currentR][currentC] = 0
            self.data[newR][newC] = 9
            self.updateNeighbors(currentR, currentC)
            self.updateNeighbors(newR, newC)
        else:
            return False
        
    def show(self, x:int, y:int):
        self.display[y][x] = True

