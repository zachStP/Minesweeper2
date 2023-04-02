from Board import Board

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
#Board.changeMineAtTo(board, self.y - 1, self.x, self.y - 2, self.x)
    def pushMine(self, board, dir):
        if dir == "up":
            if(Board.isMine(board, self.y - 1, self.x)):
                if(Board.isMine(board, self.y - 2, self.x)):
                    Board.changeDataAtTo(board, self.y - 2, self.x, 10)
                elif(Board.isValid(board, self.y - 2, self.x)):
                    Board.moveMineAtTo(board, self.y - 1, self.x, self.y - 2, self.x)
                    
        if dir == "down":
            if(Board.isMine(board, self.y + 1, self.x)):
                if(Board.isMine(board, self.y + 2, self.x)):
                    Board.changeDataAtTo(board, self.y + 2, self.x, 10)
                elif(Board.isValid(board, self.y + 2, self.x)):
                    Board.moveMineAtTo(board, self.y + 1, self.x, self.y + 2, self.x)

        if dir == "right":
            if(Board.isMine(board, self.y, self.x + 1)):
                if(Board.isMine(board, self.y, self.x + 2)):
                    Board.changeDataAtTo(board, self.y, self.x + 2, 10)
                elif(Board.isValid(board, self.y, self.x + 2)):
                    Board.moveMineAtTo(board, self.y, self.x + 1, self.y, self.x + 2)
        if dir == "left":
            if(Board.isMine(board, self.y, self.x - 1)):
                if(Board.isMine(board, self.y, self.x - 2)):
                    Board.changeDataAtTo(board, self.y, self.x - 2, 10)
                elif(Board.isValid(board, self.y, self.x - 2)):
                    Board.moveMineAtTo(board, self.y, self.x + 1, self.y, self.x - 2)

