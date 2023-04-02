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
