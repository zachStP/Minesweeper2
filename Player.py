if __name__ == "__main__":
    import main

class Player:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
        self.isDead = False

    def moveUp(self):
        if self.isDead:
            return
        if self.y - 1 >= 0:
            self.y -= 1

    def moveDown(self):
        if self.isDead:
            return
        if self.y + 1 < 16:
            self.y += 1

    def moveLeft(self):
        if self.isDead:
            return
        if self.x - 1 >= 0:
            self.x -= 1

    def moveRight(self):
        if self.isDead:
            return
        if self.x + 1 < 16:
            self.x += 1

    def kill(self):
        self.isDead = True
#board.changeMineAtTo(board, self.y - 1, self.x, self.y - 2, self.x)
    def pushMine(self, board, dir):
        cellsAtDirWithDis1 = [(self.y - 1, self.x), (self.y + 1, self.x),
                          (self.y, self.x + 1), (self.y, self.x - 1)]
        cellsAtDirWithDis2 = [(self.y - 2, self.x), (self.y + 2, self.x),
                          (self.y, self.x + 2), (self.y, self.x - 2)]
        if dir == "up":
            cellWithDis1 = cellsAtDirWithDis1[0]
            cellWithDis2 = cellsAtDirWithDis2[1]

            """if(board.isMine(board.data, self.y - 1, self.x)):
                if(board.isMine(board.data, self.y - 2, self.x)):
                    board.changeDataAtTo(self.y - 1, self.x, 0)
                    board.changeDataAtTo(self.y - 2, self.x, 10)
                elif(board.isValid(board.data, self.y - 2, self.x)):
                    board.moveMineAtTo(self.y - 1, self.x, self.y - 2, self.x)
            """        
        if dir == "down":
            if(board.isMine(board.data, self.y + 1, self.x)):
                if(board.isMine(board.data, self.y + 2, self.x)):
                    board.changeDataAtTo(self.y + 1, self.x, 0)
                    board.changeDataAtTo(self.y + 2, self.x, 10)
                elif(board.isValid(board.data, self.y + 2, self.x)):
                    board.moveMineAtTo(self.y + 1, self.x, self.y + 2, self.x)

        if dir == "right":
            if(board.isMine(board.data, self.y, self.x + 1)):
                if(board.isMine(board.data, self.y, self.x + 2)):
                    board.changeDataAtTo(self.y, self.x + 1, 0)
                    board.changeDataAtTo(self.y, self.x + 2, 10)
                elif(board.isValid(board.data, self.y, self.x + 2)):
                    board.moveMineAtTo(self.y, self.x + 1, self.y, self.x + 2)
        if dir == "left":
            if(board.isMine(board.data, self.y, self.x - 1)):
                if(board.isMine(board.data, self.y, self.x - 2)):
                    board.changeDataAtTo(self.y, self.x - 1, 0)
                    board.changeDataAtTo(self.y, self.x - 2, 10)
                elif(board.isValid(board.data, self.y, self.x - 2)):
                    board.moveMineAtTo(self.y, self.x - 1, self.y, self.x - 2)

        if(board.isMine(board.data, cellWithDis1[0], cellWithDis1[1])):
            if(board.isMine(board.data, cellWithDis2[0], cellWithDis2[1])):
                board.changeDataAtTo(cellWithDis1[0], cellWithDis1[1], 0)
                board.changeDataAtTo(cellWithDis2[0], cellWithDis2[1], 10)
            elif(board.isValid(board.data, cellWithDis2[0], cellWithDis2[1])):
                board.moveMineAtTo(cellWithDis1[0], cellWithDis1[1], cellWithDis2[0], cellWithDis2[1])

    def flag(self, board, dir):
        if dir == "up":
            if(board.isValid(board.data, self.y - 1, self.x)):
                board.changeDataAtTo(self.y - 1, self.x, -1 * board.data[self.y - 1][self.x])   
        if dir == "down":
            if(board.isValid(board.data, self.y + 1, self.x)):
                board.changeDataAtTo(self.y + 1, self.x,  -1 * board.data[self.y + 1][self.x])
        if dir == "right":
            if(board.isValid(board.data, self.y, self.x + 1)):
                board.changeDataAtTo(self.y, self.x + 1,  -1 * board.data[self.y][self.x + 1])
        if dir == "left":
            if(board.isValid(board.data, self.y, self.x - 1)):
                board.changeDataAtTo(self.y, self.x - 1,  -1 * board.data[self.y][self.x - 1])
                