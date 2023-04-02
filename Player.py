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
        if dir == "up":
            if(board.isMine(board.data, self.y - 1, self.x)):
                if(board.isMine(board.data, self.y - 2, self.x)):
                    board.changeDataAtTo(board.data, self.y - 2, self.x, 10)
                elif(board.isValid(board.data, self.y - 2, self.x)):
                    board.moveMineAtTo(self.y - 1, self.x, self.y - 2, self.x)
                    
        if dir == "down":
            if(board.isMine(board.data, self.y + 1, self.x)):
                if(board.isMine(board.data, self.y + 2, self.x)):
                    board.changeDataAtTo(board.data, self.y + 2, self.x, 10)
                elif(board.isValid(board.data, self.y + 2, self.x)):
                    board.moveMineAtTo(self.y + 1, self.x, self.y + 2, self.x)

        if dir == "right":
            if(board.isMine(board.data, self.y, self.x + 1)):
                if(board.isMine(board.data, self.y, self.x + 2)):
                    board.changeDataAtTo(board.data, self.y, self.x + 2, 10)
                elif(board.isValid(board.data, self.y, self.x + 2)):
                    board.moveMineAtTo(self.y, self.x + 1, self.y, self.x + 2)
        if dir == "left":
            print(board.isMine(board.data, self.y, self.x - 1))
            if(board.isMine(board.data, self.y, self.x - 1)):
                if(board.isMine(board.data, self.y, self.x - 2)):
                    board.changeDataAtTo(board.data, self.y, self.x - 2, 10)
                elif(board.isValid(board.data, self.y, self.x - 2)):
                    board.moveMineAtTo(self.y, self.x + 1, self.y, self.x - 2)

